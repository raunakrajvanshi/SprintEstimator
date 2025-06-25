from flask import Flask, render_template, request, jsonify, send_file, flash, redirect, url_for
from enhanced_estimator import EnhancedSprintEstimator
import os
from datetime import datetime
import json

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this in production

# Initialize the enhanced estimator
estimator = EnhancedSprintEstimator()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Collect project details from form
            project_details = {
                'project_name': request.form.get('project_name', ''),
                'description': request.form.get('description', ''),
                'total_team_size': int(request.form.get('total_team_size', 5)),
                'duration_weeks': int(request.form.get('duration_weeks', 4)),
                'priority': request.form.get('priority', 'Medium'),
                'user_stories': request.form.get('user_stories', '').split('\n') if request.form.get('user_stories') else [],
                'dependencies': request.form.get('dependencies', '').split('\n') if request.form.get('dependencies') else [],
                'risks': request.form.get('risks', '').split('\n') if request.form.get('risks') else [],
                'team_skills': request.form.get('team_skills', '').split(',') if request.form.get('team_skills') else [],
                'tech_stack': request.form.get('tech_stack', '').split(',') if request.form.get('tech_stack') else []
            }
            
            # Get AI analysis
            analysis = estimator.get_ai_analysis(project_details)
            
            # Generate spreadsheet
            if 'error' not in analysis:
                spreadsheet_file = estimator.generate_sprint_spreadsheet(analysis, project_details)
                
                return render_template('results.html', 
                                     analysis=analysis, 
                                     project_details=project_details,
                                     spreadsheet_file=spreadsheet_file)
            else:
                flash(f"Error in analysis: {analysis['error']}", 'error')
                return redirect(url_for('index'))
                
        except Exception as e:
            flash(f"An error occurred: {str(e)}", 'error')
            return redirect(url_for('index'))
    
    return render_template('index.html')

@app.route('/download/<filename>')
def download_file(filename):
    """Download generated spreadsheet"""
    try:
        return send_file(filename, as_attachment=True)
    except Exception as e:
        flash(f"Error downloading file: {str(e)}", 'error')
        return redirect(url_for('index'))

@app.route('/api/estimate', methods=['POST'])
def api_estimate():
    """API endpoint for programmatic access"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        analysis = estimator.get_ai_analysis(data)
        
        if 'error' in analysis:
            return jsonify(analysis), 500
        
        # Generate spreadsheet
        spreadsheet_file = estimator.generate_sprint_spreadsheet(analysis, data)
        
        return jsonify({
            'analysis': analysis,
            'spreadsheet_file': spreadsheet_file,
            'download_url': f'/download/{spreadsheet_file}'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/historical-insights')
def historical_insights():
    """Display historical data insights"""
    try:
        insights = estimator.analyze_historical_patterns()
        return render_template('insights.html', insights=insights)
    except Exception as e:
        flash(f"Error loading insights: {str(e)}", 'error')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

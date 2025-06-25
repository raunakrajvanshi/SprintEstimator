#!/usr/bin/env python3
"""
Demo script for the Enhanced Sprint Estimator
This script demonstrates how to use the API programmatically
"""

import json
from enhanced_estimator import EnhancedSprintEstimator

def demo_sprint_estimation():
    """Demonstrate the sprint estimation functionality"""
    
    # Sample project data
    project_details = {
        'project_name': 'E-commerce Platform Redesign',
        'description': 'Complete redesign of our e-commerce platform with modern UI/UX, improved performance, and mobile responsiveness',
        'total_team_size': 6,
        'duration_weeks': 12,
        'priority': 'High',
        'user_stories': [
            'As a customer, I want to browse products with an intuitive interface',
            'As a customer, I want to search and filter products efficiently',
            'As a customer, I want to add items to cart and checkout securely',
            'As a customer, I want to track my order status',
            'As an admin, I want to manage product inventory',
            'As an admin, I want to view sales analytics and reports'
        ],
        'dependencies': [
            'Payment gateway integration',
            'Inventory management API',
            'Email notification service',
            'CDN setup for image optimization'
        ],
        'risks': [
            'Third-party payment service downtime',
            'Legacy system integration complexity',
            'Performance requirements under high load',
            'Mobile device compatibility issues'
        ],
        'team_skills': ['React', 'Node.js', 'Python', 'AWS', 'MongoDB', 'Docker'],
        'tech_stack': ['React', 'Express.js', 'MongoDB', 'Redis', 'Docker', 'AWS']
    }
    
    print("🚀 Enhanced Sprint Estimator Demo")
    print("=" * 50)
    
    # Initialize the estimator
    print("Initializing Enhanced Sprint Estimator...")
    estimator = EnhancedSprintEstimator()
    
    print(f"📋 Project: {project_details['project_name']}")
    print(f"👥 Team Size: {project_details['total_team_size']}")
    print(f"⏱️ Duration: {project_details['duration_weeks']} weeks")
    print(f"🎯 Priority: {project_details['priority']}")
    print()
    
    # Demonstrate historical analysis
    print("📊 Historical Data Analysis:")
    historical_insights = estimator.analyze_historical_patterns()
    print(historical_insights[:500] + "..." if len(historical_insights) > 500 else historical_insights)
    print()
    
    # Note: Actual AI analysis requires OpenAI API key
    print("💡 To get full AI analysis, you need to:")
    print("1. Set up your OpenAI API key in .env file")
    print("2. Run: analysis = estimator.get_ai_analysis(project_details)")
    print("3. Generate spreadsheet: estimator.generate_sprint_spreadsheet(analysis, project_details)")
    print()
    
    # Demonstrate spreadsheet generation with mock data
    print("📈 Generating demo spreadsheet...")
    mock_analysis = {
        "project_overview": "This is a high-priority e-commerce platform redesign project...",
        "sprint_breakdown": "Sprint 1: UI/UX Foundation, Sprint 2: Core Features...",
        "bottlenecks": "Potential bottlenecks include payment integration and performance optimization...",
        "resources": "Team allocation optimized for parallel development streams...",
        "risks": "Key risks mitigated through early prototyping and testing...",
        "timeline": "12-week timeline with 6 two-week sprints and buffer periods..."
    }
    
    try:
        spreadsheet_file = estimator.generate_sprint_spreadsheet(mock_analysis, project_details)
        print(f"✅ Demo spreadsheet generated: {spreadsheet_file}")
        print("📋 The spreadsheet includes 6 comprehensive sheets:")
        print("   • Project Overview")
        print("   • Sprint Breakdown") 
        print("   • Bottleneck Analysis")
        print("   • Resource Planning")
        print("   • Risk Assessment")
        print("   • Timeline & Milestones")
    except Exception as e:
        print(f"⚠️ Error generating spreadsheet: {e}")
    
    print()
    print("🌐 To use the web interface:")
    print("1. Run: python3 app.py")
    print("2. Open: http://localhost:5000")
    print("3. Fill in your project details")
    print("4. Get comprehensive analysis and downloadable Excel report")
    
    return project_details

if __name__ == "__main__":
    demo_sprint_estimation() 
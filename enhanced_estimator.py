from openai import OpenAI
import os
import json
import pandas as pd
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Any
import numpy as np
from dotenv import load_dotenv
from prompt_templates import get_comprehensive_prompt, get_bottleneck_prompt, get_resource_optimization_prompt

load_dotenv()

class EnhancedSprintEstimator:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.historical_data = self.load_historical_data()
        
    def load_historical_data(self) -> pd.DataFrame:
        """Load and prepare historical sprint data"""
        try:
            with open('historical_sprint_data.json', 'r') as f:
                data = json.load(f)
            return pd.DataFrame(data)
        except Exception as e:
            print(f"Error loading historical data: {e}")
            return pd.DataFrame()
    
    def generate_comprehensive_prompt(self, project_details: Dict[str, Any]) -> str:
        """Generate a comprehensive prompt for OpenAI analysis using advanced templates"""
        
        # Analyze historical patterns
        historical_insights = self.analyze_historical_patterns()
        
        # Use the advanced comprehensive prompt template
        return get_comprehensive_prompt(project_details, historical_insights)
    
    def analyze_historical_patterns(self) -> str:
        """Analyze historical data to provide insights"""
        if self.historical_data.empty:
            return "No historical data available for analysis."
        
        # Calculate key metrics
        avg_velocity = self.historical_data['Actual_Story_Points'].mean()
        avg_hours_per_point = self.historical_data['Actual_Hours'].mean() / self.historical_data['Actual_Story_Points'].mean()
        
        # Identify common bottlenecks
        risk_analysis = self.historical_data['Risks'].explode().value_counts().head(5)
        dependency_analysis = self.historical_data['Dependencies'].explode().value_counts().head(5)
        
        insights = f"""
        HISTORICAL PERFORMANCE METRICS:
        - Average Story Points per Sprint: {avg_velocity:.1f}
        - Average Hours per Story Point: {avg_hours_per_point:.1f}
        - Total Stories Analyzed: {len(self.historical_data)}
        
        COMMON BOTTLENECKS:
        {risk_analysis.to_string()}
        
        FREQUENT DEPENDENCIES:
        {dependency_analysis.to_string()}
        """
        
        return insights
    
    def get_ai_analysis(self, project_details: Dict[str, Any]) -> Dict[str, Any]:
        """Get comprehensive AI analysis of the project"""
        prompt = self.generate_comprehensive_prompt(project_details)
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an expert Agile Project Manager specializing in sprint planning, bottleneck identification, and resource optimization."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=4000,
                temperature=0.3
            )
            
            # Try to parse as JSON, fallback to text processing
            content = response.choices[0].message.content.strip()
            try:
                return json.loads(content)
            except json.JSONDecodeError:
                return self.parse_text_response(content)
                
        except Exception as e:
            return {"error": f"Failed to get AI analysis: {str(e)}"}
    
    def get_bottleneck_analysis(self, project_details: Dict[str, Any]) -> Dict[str, Any]:
        """Get specialized bottleneck analysis"""
        prompt = get_bottleneck_prompt(project_details)
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a specialized Project Bottleneck Analyst with expertise in identifying and resolving constraints."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=2000,
                temperature=0.2
            )
            
            return {"bottleneck_analysis": response.choices[0].message.content.strip()}
            
        except Exception as e:
            return {"error": f"Failed to get bottleneck analysis: {str(e)}"}
    
    def get_resource_optimization(self, project_details: Dict[str, Any]) -> Dict[str, Any]:
        """Get specialized resource optimization analysis"""
        prompt = get_resource_optimization_prompt(project_details)
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a Resource Planning Specialist with expertise in team allocation and capacity optimization."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=2000,
                temperature=0.2
            )
            
            return {"resource_optimization": response.choices[0].message.content.strip()}
            
        except Exception as e:
            return {"error": f"Failed to get resource optimization: {str(e)}"}
    
    def parse_text_response(self, content: str) -> Dict[str, Any]:
        """Parse text response into structured format"""
        return {
            "raw_analysis": content,
            "project_overview": self.extract_section(content, "PROJECT OVERVIEW"),
            "sprint_breakdown": self.extract_section(content, "SPRINT BREAKDOWN"),
            "bottleneck_analysis": self.extract_section(content, "BOTTLENECK ANALYSIS"),
            "resource_planning": self.extract_section(content, "RESOURCE PLANNING"),
            "risk_assessment": self.extract_section(content, "RISK ASSESSMENT"),
            "dependencies_mapping": self.extract_section(content, "DEPENDENCIES MAPPING"),
            "timeline_milestones": self.extract_section(content, "TIMELINE & MILESTONES"),
            "recommendations": self.extract_section(content, "RECOMMENDATIONS")
        }
    
    def extract_section(self, content: str, section_name: str) -> str:
        """Extract a specific section from the response"""
        try:
            start_idx = content.find(section_name)
            if start_idx == -1:
                return "Section not found"
            
            # Find the next section or end of content
            next_section_idx = content.find("**", start_idx + len(section_name))
            if next_section_idx == -1:
                return content[start_idx:]
            else:
                return content[start_idx:next_section_idx]
        except:
            return "Error extracting section"
    
    def generate_sprint_spreadsheet(self, analysis: Dict[str, Any], project_details: Dict[str, Any]) -> str:
        """Generate Excel spreadsheet with sprint planning data"""
        try:
            # Create multiple sheets for comprehensive reporting
            filename = f"Sprint_Plan_{project_details.get('project_name', 'Project')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
            
            with pd.ExcelWriter(filename, engine='openpyxl') as writer:
                # Sheet 1: Project Overview
                overview_data = {
                    'Project Name': [project_details.get('project_name', 'N/A')],
                    'Description': [project_details.get('description', 'N/A')],
                    'Team Size': [project_details.get('total_team_size', 'N/A')],
                    'Duration (weeks)': [project_details.get('duration_weeks', 'N/A')],
                    'Priority': [project_details.get('priority', 'Medium')],
                    'Generated On': [datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
                }
                pd.DataFrame(overview_data).to_excel(writer, sheet_name='Project Overview', index=False)
                
                # Sheet 2: Sprint Breakdown
                sprint_data = self.create_sprint_breakdown_data(analysis, project_details)
                pd.DataFrame(sprint_data).to_excel(writer, sheet_name='Sprint Breakdown', index=False)
                
                # Sheet 3: Bottleneck Analysis
                bottleneck_data = self.create_bottleneck_data(analysis)
                pd.DataFrame(bottleneck_data).to_excel(writer, sheet_name='Bottleneck Analysis', index=False)
                
                # Sheet 4: Resource Planning
                resource_data = self.create_resource_planning_data(analysis, project_details)
                pd.DataFrame(resource_data).to_excel(writer, sheet_name='Resource Planning', index=False)
                
                # Sheet 5: Risk Assessment
                risk_data = self.create_risk_assessment_data(analysis)
                pd.DataFrame(risk_data).to_excel(writer, sheet_name='Risk Assessment', index=False)
                
                # Sheet 6: Timeline & Milestones
                timeline_data = self.create_timeline_data(analysis, project_details)
                pd.DataFrame(timeline_data).to_excel(writer, sheet_name='Timeline & Milestones', index=False)
            
            return filename
            
        except Exception as e:
            return f"Error generating spreadsheet: {str(e)}"
    
    def create_sprint_breakdown_data(self, analysis: Dict[str, Any], project_details: Dict[str, Any]) -> List[Dict]:
        """Create sprint breakdown data for spreadsheet"""
        # Sample sprint breakdown based on typical project structure
        sprints = []
        total_stories = len(project_details.get('user_stories', []))
        stories_per_sprint = max(1, total_stories // int(project_details.get('duration_weeks', 4)))
        
        for i in range(1, int(project_details.get('duration_weeks', 4)) + 1):
            sprint = {
                'Sprint Number': i,
                'Sprint Goal': f'Sprint {i} deliverables',
                'Duration (weeks)': 2,
                'Stories Count': stories_per_sprint,
                'Estimated Story Points': stories_per_sprint * 5,  # Assuming avg 5 points per story
                'Estimated Hours': stories_per_sprint * 20,  # Assuming 20 hours per story
                'Team Capacity': project_details.get('total_team_size', 5) * 80,  # 80 hours per person per 2-week sprint
                'Capacity Utilization': f"{(stories_per_sprint * 20) / (project_details.get('total_team_size', 5) * 80) * 100:.1f}%",
                'Key Deliverables': f'Features for Sprint {i}',
                'Dependencies': 'API integrations, Testing' if i > 1 else 'Initial setup'
            }
            sprints.append(sprint)
        
        return sprints
    
    def create_bottleneck_data(self, analysis: Dict[str, Any]) -> List[Dict]:
        """Create bottleneck analysis data"""
        bottlenecks = [
            {
                'Bottleneck Type': 'Technical Debt',
                'Description': 'Legacy code integration challenges',
                'Impact Level': 'High',
                'Affected Sprints': '2-4',
                'Mitigation Strategy': 'Dedicated refactoring time, Code review sessions',
                'Timeline Impact': '+2 days',
                'Owner': 'Tech Lead'
            },
            {
                'Bottleneck Type': 'Resource Constraint',
                'Description': 'Limited backend developers',
                'Impact Level': 'Medium',
                'Affected Sprints': '1-3',
                'Mitigation Strategy': 'Cross-training, External consultant',
                'Timeline Impact': '+1 week',
                'Owner': 'Project Manager'
            },
            {
                'Bottleneck Type': 'External Dependency',
                'Description': 'Third-party API availability',
                'Impact Level': 'High',
                'Affected Sprints': '3-4',
                'Mitigation Strategy': 'Mock services, Parallel development',
                'Timeline Impact': '+3 days',
                'Owner': 'Technical Architect'
            }
        ]
        return bottlenecks
    
    def create_resource_planning_data(self, analysis: Dict[str, Any], project_details: Dict[str, Any]) -> List[Dict]:
        """Create resource planning data"""
        team_size = project_details.get('total_team_size', 5)
        resources = []
        
        roles = ['Frontend Developer', 'Backend Developer', 'QA Engineer', 'DevOps Engineer', 'UI/UX Designer']
        for i, role in enumerate(roles[:team_size]):
            resource = {
                'Role': role,
                'Allocated FTE': 1.0,
                'Sprint 1 Utilization': '90%',
                'Sprint 2 Utilization': '95%',
                'Sprint 3 Utilization': '85%',
                'Sprint 4 Utilization': '80%',
                'Skills Required': 'React, Node.js' if 'Developer' in role else role.replace(' ', ', '),
                'Skill Gap': 'None' if i < 2 else 'Training needed',
                'Peak Load Period': f'Sprint {i % 4 + 1}',
                'Backup Resource': 'Cross-trained team member'
            }
            resources.append(resource)
        
        return resources
    
    def create_risk_assessment_data(self, analysis: Dict[str, Any]) -> List[Dict]:
        """Create risk assessment data"""
        risks = [
            {
                'Risk Category': 'Technical',
                'Risk Description': 'Integration complexity with legacy systems',
                'Probability': 'Medium',
                'Impact': 'High',
                'Risk Score': 6,
                'Mitigation Plan': 'Early prototyping, Technical spikes',
                'Contingency Buffer': '5 days',
                'Owner': 'Technical Lead',
                'Status': 'Active'
            },
            {
                'Risk Category': 'Resource',
                'Risk Description': 'Key team member unavailability',
                'Probability': 'Low',
                'Impact': 'High',
                'Risk Score': 4,
                'Mitigation Plan': 'Knowledge sharing, Documentation',
                'Contingency Buffer': '3 days',
                'Owner': 'Project Manager',
                'Status': 'Monitored'
            },
            {
                'Risk Category': 'External',
                'Risk Description': 'Third-party service downtime',
                'Probability': 'Medium',
                'Impact': 'Medium',
                'Risk Score': 4,
                'Mitigation Plan': 'Service level agreements, Backup providers',
                'Contingency Buffer': '2 days',
                'Owner': 'Technical Architect',
                'Status': 'Active'
            }
        ]
        return risks
    
    def create_timeline_data(self, analysis: Dict[str, Any], project_details: Dict[str, Any]) -> List[Dict]:
        """Create timeline and milestones data"""
        start_date = datetime.now()
        timeline = []
        
        for i in range(1, int(project_details.get('duration_weeks', 4)) + 1):
            sprint_start = start_date + timedelta(weeks=(i-1)*2)
            sprint_end = sprint_start + timedelta(weeks=2)
            
            milestone = {
                'Sprint': i,
                'Start Date': sprint_start.strftime('%Y-%m-%d'),
                'End Date': sprint_end.strftime('%Y-%m-%d'),
                'Milestone': f'Sprint {i} Demo',
                'Deliverables': f'Sprint {i} features completed',
                'Dependencies': 'Previous sprint completion',
                'Buffer Days': 2,
                'Critical Path': 'Yes' if i in [2, 4] else 'No',
                'Stakeholder Review': sprint_end.strftime('%Y-%m-%d')
            }
            timeline.append(milestone)
        
        return timeline 
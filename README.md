# Sprint Estimator & Project Planner

An AI-powered sprint estimation and project planning tool that leverages OpenAI's GPT models to provide comprehensive project analysis, bottleneck identification, resource planning, and timeline optimization.

## Features

### Comprehensive Analysis
- **Sprint Breakdown**: Detailed sprint planning with story points, hours, and capacity analysis
- **Bottleneck Identification**: AI-powered analysis to identify and mitigate project bottlenecks
- **Resource Planning**: Optimal team allocation and capacity utilization recommendations
- **Risk Assessment**: Comprehensive risk analysis with mitigation strategies
- **Timeline & Milestones**: Detailed project timeline with key milestones and dependencies
- **Excel Export**: Downloadable comprehensive project documentation and planning sheets

### Multi-Sheet Excel Reports
The tool generates comprehensive Excel reports with 6 detailed sheets:
1. **Project Overview** - Executive summary and project details
2. **Sprint Breakdown** - Detailed sprint planning with story points and capacity
3. **Bottleneck Analysis** - Identified constraints and mitigation strategies
4. **Resource Planning** - Team allocation and utilization optimization
5. **Risk Assessment** - Risk matrix with probability, impact, and mitigation plans
6. **Timeline & Milestones** - Project schedule with dependencies and critical path

### AI-Powered Insights
- Historical data analysis for performance benchmarking
- Intelligent bottleneck prediction and mitigation strategies
- Resource optimization recommendations
- Risk probability and impact assessment
- Timeline optimization with buffer recommendations

##  Installation

### Prerequisites
- Python 3.8+
- OpenAI API key

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd SprintEstimator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` file and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

## Usage

### Web Interface

1. **Project Information**
   - Enter project name and description
   - Set project priority level

2. **Team & Timeline**
   - Specify team size and project duration
   - List team skills and technology stack

3. **User Stories**
   - Enter user stories (one per line)
   - Describe acceptance criteria and requirements

4. **Dependencies & Risks**
   - List known dependencies
   - Identify potential risks

5. **Generate Analysis**
   - Click "Generate Sprint Plan & Analysis"
   - Review the comprehensive analysis
   - Download the Excel report

### API Endpoint

The tool also provides a REST API for programmatic access:

```bash
POST /api/estimate
Content-Type: application/json

{
  "project_name": "E-commerce Platform",
  "description": "Building a modern e-commerce platform",
  "total_team_size": 6,
  "duration_weeks": 12,
  "priority": "High",
  "user_stories": [
    "As a user, I want to browse products",
    "As a user, I want to add items to cart"
  ],
  "dependencies": ["Payment gateway", "Inventory API"],
  "risks": ["Third-party integration", "Performance requirements"],
  "team_skills": ["React", "Node.js", "Python"],
  "tech_stack": ["React", "Express", "MongoDB"]
}
```

## Historical Data Analysis

The tool analyzes historical sprint data to provide insights:
- Average story points per sprint
- Hours per story point ratios
- Common bottlenecks and dependencies
- Performance trends and patterns

Access historical insights at `/historical-insights`

## Configuration

### Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `FLASK_ENV`: Flask environment (development/production)
- `FLASK_DEBUG`: Enable debug mode (true/false)
- `SECRET_KEY`: Flask secret key for sessions

### Customization
- Modify `historical_sprint_data.json` to include your organization's data
- Adjust AI prompts in `enhanced_estimator.py` for domain-specific analysis
- Customize spreadsheet templates in the `create_*_data` methods

## Project Structure

```
SprintEstimator/
├── app.py                          # Flask application
├── enhanced_estimator.py           # Enhanced AI estimator with comprehensive features
├── estimator.py                    # Original estimator (legacy)
├── data_loader.py                  # Data loading utilities
├── historical_sprint_data.json     # Historical sprint data for analysis
├── requirements.txt                # Python dependencies
├── .env.example                    # Environment configuration template
├── README.md                       # This file
└── templates/
    ├── index.html                  # Main form interface
    ├── results.html                # Analysis results display
    └── insights.html               # Historical insights display
```

## Advanced Features

### Bottleneck Analysis
- **Technical Bottlenecks**: Code complexity, legacy system integration
- **Resource Bottlenecks**: Skill gaps, capacity constraints
- **Dependency Bottlenecks**: External services, API availability
- **Process Bottlenecks**: Approval workflows, testing cycles

### Resource Optimization
- Team member allocation across sprints
- Skill gap identification and training recommendations
- Capacity utilization optimization
- Peak load period management

### Risk Management
- Probability and impact assessment
- Mitigation strategy recommendations
- Contingency buffer calculations
- Risk monitoring and tracking

## Use Cases

### Project Managers
- Accurate sprint planning and estimation
- Resource allocation optimization
- Risk identification and mitigation
- Timeline and milestone planning

### Development Teams
- Workload distribution insights
- Skill development recommendations
- Bottleneck awareness and resolution
- Performance benchmarking

### Stakeholders
- Executive summaries and progress tracking
- Resource investment planning
- Timeline and budget optimization
- Risk visibility and management

## Future Enhancements

- **Integration with Jira/GitHub** for automated data collection
- **Machine Learning Models** for improved estimation accuracy
- **Real-time Collaboration** features for team planning
- **Advanced Analytics** with predictive modeling
- **Mobile Application** for on-the-go access
- **Custom Templates** for different project types

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please:
1. Check the documentation
2. Review existing issues
3. Create a new issue with detailed information
4. Contact the development team

## 🔗 Resources

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Agile Sprint Planning Best Practices](https://www.atlassian.com/agile/scrum/sprint-planning)
- [Project Risk Management](https://www.pmi.org/learning/library/risk-management-project-success-6467)

---

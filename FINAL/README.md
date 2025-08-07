# TDS Data Analyst Agent

A powerful AI-powered data analyst agent that can process various data sources and provide comprehensive analysis with visualizations.

## Features

- **Multi-source data processing**: CSV files, Wikipedia scraping, DuckDB/Parquet support
- **AI-powered analysis**: Uses Google Gemini 2.5 Flash for intelligent data analysis
- **Visualization generation**: Creates charts and graphs encoded as base64 images
- **FastAPI endpoint**: RESTful API for easy integration
- **Streamlit UI**: User-friendly web interface for easy interaction
- **Robust error handling**: Multiple fallback strategies for reliability
- **3-minute timeout protection**: Ensures responses within time limits

## Quick Setup

1. **Install dependencies**:
```bash
pip install -r requirements.txt
```

2. **Set your Gemini API key**:
```bash
export GEMINI_API_KEY="your_api_key_here"
```

3. **Start the API server**:
```bash
uvicorn main:app --host 0.0.0.0 --port 8080
```

4. **Start the Streamlit UI** (optional):
```bash
streamlit run streamlit_app.py --server.port 8501
```

## Usage

### API Usage

Send a POST request with a text file containing your data analysis question:

```bash
curl -X POST "http://localhost:8080/api" -F "file=@question.txt"
```

### Streamlit UI Usage

1. Open your browser to `http://localhost:8501`
2. Upload a `.txt` file with your question
3. Click "Run Analysis"
4. View the results with visualizations

### Example Questions

The repository includes three test questions:
- `test_question_1.txt`: Tips dataset analysis
- `test_question_2.txt`: Wikipedia scraping (highest grossing films)
- `test_question_3.txt`: Indian High Court judgments analysis

## API Response Format

The API returns a JSON array with exactly 4 elements as requested in the problem statement:

```json
[
  27,
  "Sun", 
  "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA...",
  0.676
]
```

## Supported Data Sources

- **CSV files**: Direct URL access to CSV data
- **Wikipedia**: Web scraping and data extraction
- **DuckDB/Parquet**: S3 and local parquet file support
- **Synthetic data**: Generated datasets for analysis

## Testing

The implementation has been tested with all three sample questions from the problem statement:

1. **Tips Dataset Analysis**: ✅ Working
2. **Wikipedia Film Data**: ✅ Working  
3. **Indian Court Data**: ✅ Working

All tests return proper JSON responses with base64-encoded visualizations under 100KB.

## Deployment

The application is configured for deployment on Render.com with the included `render.yaml` configuration.

## License

MIT License
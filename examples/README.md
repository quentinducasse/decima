# DECIMA Usage Examples

This directory contains examples demonstrating how to use DECIMA programmatically.

## Basic Usage (`basic_usage.py`)

A complete example showing the DECIMA workflow with verbose output:
- QUIET: Query interpretation and focus detection
- EMMA: Knowledge Graph entity extraction
- OTACON: LLM reasoning and code generation
- EVA: Secure code execution

### Running the Example

**In Docker (recommended):**
```bash
docker compose exec app python3 examples/basic_usage.py
```

**Locally (requires Python 3.10+ and dependencies):**
```bash
pip install -e .
python3 examples/basic_usage.py
```

### Expected Output

The example displays:
1. Environment configuration (API key, demo mode status)
2. EMMA Knowledge Graph context (extracted entities)
3. OTACON LLM response (explanation + generated code)
4. EVA execution results (stdout, plots)
5. Workflow logs

## Configuration

### API Key

Set your OpenAI API key in `.env.docker`:
```
OPENAI_API_KEY=your-key-here
DEMO_MODE=false
```

### Demo Mode

To test without an API key, set `DEMO_MODE=true` in `.env.docker`.
Demo mode returns a fixed example without calling the LLM.

## Sample PTRAC Files

Sample files are included in `data/ptrac_samples/`:
- `basic_ptrac_example_decima_ascii.ptrac` - ASCII format example

## More Information

- Main documentation: See root `README.md`
- Technical docs: `doc/`
- JOSS paper: `paper.md`

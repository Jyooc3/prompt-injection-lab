# Prompt-Injection Lab

A practical AI security project exploring prompt-injection attacks, basic defensive controls, and automated testing of an LLM-powered chatbot.

## 1. Project Overview

This project implements a simulated banking assistant and evaluates its response to 20 prompt-injection test prompts. It compares a baseline implementation against a defended implementation using three layers of protection.

The project uses Python and the Groq API with the `openai/gpt-oss-20b` model.

## 2. Objectives

- Build an LLM-powered chatbot in Python.
- Develop a collection of 20 prompt-injection test prompts.
- Automate testing in baseline and defended modes.
- Implement system-prompt hardening, input filtering, and output filtering.
- Record responses in CSV files and compare test results.
- Identify the limitations of simple prompt-injection defences.

## 3. Architecture

The application follows this workflow:

1. A user submits a message.
2. In defended mode, an input filter checks for selected suspicious phrases.
3. The message and system prompt are sent to the LLM when permitted.
4. The generated response is checked for the configured secret in its recognised representations.
5. The response or a refusal message is returned.
6. The testing script records the results in CSV format.

## 4. Technologies

- Python
- Groq API
- Groq Python SDK
- `openai/gpt-oss-20b`
- Git and GitHub
- CSV for experiment results

## 5. Project Structure

```text
PROJECT/
├── bot.py
├── attacks.py
├── tester.py
├── results_baseline.csv
├── results_defended.csv
├── README.md
└── .gitignore
```

## 6. Defensive Controls

### Defence 1: System-prompt hardening

The defended mode uses more explicit instructions about confidentiality and treats user messages as untrusted input.

### Defence 2: Input filtering

A keyword-based filter blocks messages containing selected phrases associated with prompt injection.

### Defence 3: Output filtering

A response check looks for the configured secret in its normalised form and a specific Base64 representation. If detected, the chatbot returns a refusal message.

These controls demonstrate basic defensive concepts. They are not a guarantee against prompt injection and should not be considered production-ready security controls.

## 7. Testing Methodology

The automated test suite runs 20 prompts against both baseline and defended modes.

The tester records the prompt, response, direct-leak detection result, and request status in CSV files.

### Recorded Results

| Measurement | Baseline | Defended |
|---|---:|---:|
| Tests completed | 20/20 | 20/20 |
| Detected direct leaks | 0 | 0 |
| Detected direct-leak rate | 0% | 0% |

The initial experiment detected no direct leaks in either mode.

These results do not demonstrate a measurable improvement from the added defences because the baseline also recorded zero detected leaks.

The detection method is limited: it may miss indirect disclosure, alternative encodings, or other representations of sensitive information. Further testing is required before drawing broader security conclusions.

## 8. Setup

### Prerequisites

- Python installed on Windows
- A Groq API key
- Git
- Internet access

### Install the dependency

```powershell
python -m pip install groq
```

Configure `GROQ_API_KEY` as an environment variable before running the application. Never hard-code or commit the API key.

### Run the chatbot

Baseline mode:

```powershell
python bot.py
```

Defended mode:

```powershell
python bot.py defended
```

Exit the interactive chatbot by typing `exit` or `quit`.

### Run automated tests

```powershell
python tester.py
```

The tester creates or updates `results_baseline.csv` and `results_defended.csv`.

## 9. Limitations and Future Improvements

- Expand the attack suite to include more diverse and previously unseen prompts.
- Improve leak detection to recognise indirect disclosures and additional encodings.
- Measure false positives and false negatives.
- Separate model behaviour from the effects of each defensive layer.
- Repeat tests to account for model variability.
- Use structured evaluation metrics and retain error records.
- Avoid placing real credentials or sensitive information in model prompts.
- Add automated unit tests for the filtering functions.

## 10. Ethical Considerations

Testing is limited to a self-developed chatbot using a dummy secret. The project is intended for educational AI security research. No real credentials or third-party systems should be targeted.

## 11. Conclusion

This project demonstrates a basic workflow for testing an LLM-powered chatbot against prompt-injection attempts. It includes baseline and defended modes, three defensive controls, an automated test harness, and CSV-based result recording.

The initial experiment recorded zero detected direct leaks in both modes. Additional experiments are needed to assess the effectiveness and limitations of the defensive controls.

---

**Project status:** Educational prototype. Results reflect the implemented tests and detection method, not a comprehensive security assessment.

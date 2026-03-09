# Conflict Detection AI Agent

An AI-powered tool that detects logical contradictions in text using a local LLaMA model via Ollama.

## Features

- Detects contradictions in natural language text
- Batch processing of multiple inputs
- Structured JSON output
- Runs locally using LLaMA (no external API)

## Architecture

User Input → Batch Processor → LLM Conflict Detector → JSON Output

## Tech Stack

![Python](https://img.shields.io/badge/Python-3.10-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![LLM](https://img.shields.io/badge/LLM-Large%20Language%20Model-purple)
![AI](https://img.shields.io/badge/AI-Artificial%20Intelligence-orange)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-black)
![NLP](https://img.shields.io/badge/NLP-Natural%20Language%20Processing-blueviolet)

## Project Structure

Conflict_agent/
│
├── main.py
├── batch_processor.py
├── detector.py
├── inputs.txt
├── requirements.txt

## Installation

Clone the repository

git clone https://github.com/praveen819/conflict-detection-agent.git

Install dependencies

pip install -r requirements.txt

Start Ollama

ollama serve

Run the project

python main.py

## Example Input

The system must allow guest users to access all features.
Only registered users can access premium features.

## Example Output

{
  "conflicts": [
    {
      "statement_1": "...",
      "statement_2": "...",
      "severity": "high"
    }
  ]
}

# agenticframeworkaccesorialsaccessorial-agent-poc/
│
├── app.py                  # FastAPI entrypoint (your executable)
├── agent.py                # core recommendation logic
├── evaluation.py           # eval logic (precision/recall/F1)
│
├── templates/
│   └── index.html          # UI (your demo layer)
│
├── data/
│   └── eval_dataset.csv    # offline evaluation dataset
│
├── requirements.txt        # dependencies
├── README.md               # MOST IMPORTANT FILE
├── .env.example            # env variables (kill switch etc.)
│
├── demo/
│   ├── screenshots/        # UI screenshots
│   └── sample_requests.json
│
└── docs/
    └── architecture.md     # optional but high signal
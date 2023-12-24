# Job Application Tracker

A simple Python script to fetch job application details from Gmail and store them in an Excel file.

## Why Job Application Tracker?

Job Application Tracker is designed to simplify the process of managing and tracking job applications. When job hunting, it's common to apply to multiple positions, and keeping track of the application status, interview details, and responses can become overwhelming. This script automates the process by extracting relevant information from your Gmail and organizing it into a structured Excel file, providing you with a centralized view of your job applications.

## Problem Statement

- **Overwhelmed by Job Applications:** Managing numerous job applications can be challenging, leading to confusion about which positions you've applied to and their current status.
  
- **Missed Opportunities:** Without a systematic approach, you may miss important interview calls or forget to follow up on applications.

- **Lack of Organization:** Storing job application details in scattered emails makes it difficult to have a comprehensive overview of your job search progress.

## Features

- **Automated Data Extraction:** The script automatically fetches relevant information from Gmail, including job application status, interview details, and responses.

- **Excel File Organization:** Job application details are stored in a structured Excel file (`job_applications.xlsx`), providing a clear overview of your applications.

- **Customizable:** The script is easily customizable to adapt to different email formats and job application content.

## Getting Started

### Prerequisites

Before running the script, make sure you have the following set up:

- [Python](https://www.python.org/downloads/) installed on your machine.
- A [Google Cloud Project](https://console.cloud.google.com/) with the Gmail API enabled.
- `credentials.json` file obtained from the Google Cloud Console.

### Setup Instructions

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/job-application-tracker.git
    ```

2. Navigate to the project directory:

    ```bash
    cd job-application-tracker
    ```

3. Create a virtual environment:

    ```bash
    python -m venv my_project_venv
    ```

4. Activate the virtual environment:

    - On Windows:

      ```bash
      my_project_venv\Scripts\activate
      ```

    - On macOS/Linux:

      ```bash
      source my_project_venv/bin/activate
      ```

5. Install required libraries:

    ```bash
    pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
    ```

6. Move `credentials.json` into the project directory.

### Running the Script

1. Ensure your virtual environment is activated.

2. Run the script:

    ```bash
    python job_application_tracker.py
    ```

3. Follow the on-screen instructions to authorize the script.

4. Check the generated `job_applications.xlsx` file for your job application details.

## Customization

- Modify the script as needed based on your email subjects and content.
- Customize the Excel file structure in the `process_email` function.

## Troubleshooting

- If you encounter issues, refer to the [Troubleshooting](#troubleshooting) section in the script or seek help on [GitHub Issues](https://github.com/your-username/job-application-tracker/issues).

## Contributions

Contributions are welcome! If you have ideas for improvements or new features, please open an issue to discuss them. If you'd like to contribute directly, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

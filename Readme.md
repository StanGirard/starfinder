# StarFinder: GitHub Forks & User Insights

Welcome to StarFinder, a powerful tool designed to illuminate the universe of GitHub repositories by tracking forks and extracting comprehensive user information. Aimed at developers, data analysts, and open-source enthusiasts, StarFinder provides a window into the collaboration and community dynamics surrounding popular repositories. By leveraging this tool, users can uncover patterns, identify key contributors, and gain insights into the broader impact of a project.

## Features

- **Fork Crawler:** Efficiently navigates through the forks of a specified GitHub repository, compiling a detailed list of these forks along with their metadata.
- **User Information Extraction:** Goes beyond forks to fetch in-depth information about the users who have forked the repository, including their profiles, contributions, and engagement within the GitHub ecosystem.
- **Data Visualization:** Integrates with a Streamlit application, offering an intuitive interface for uploading, viewing, and analyzing the collected data in a structured and user-friendly format.

## Getting Started

To embark on your journey with StarFinder, ensure you have the following prerequisites in place:

### Prerequisites

- Python 3.6 or higher
- pip for installing dependencies

### Installation

1. Clone this repository to your local machine.
2. Install the required dependencies by running:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up a `.env` file based on the `.env_example` provided, ensuring you add your own GitHub token to authenticate API requests.

### Usage

StarFinder operates in two main stages: data collection and data visualization.

#### Data Collection

1. Run `main.py` to start the data collection process. Replace `"quivrhq/quivr"` in the `get_forks` function call with the repository you're interested in.

    ```bash
    python main.py
    ```

2. The script will first gather information about all forks of the specified repository, saving the data to `forks.csv`.
3. Next, it will extract detailed user information for each fork's owner, saving this data to `user_info.csv`.

#### Data Visualization with Streamlit

1. Launch the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. Use the sidebar to navigate between "Forks" and "User Info" pages.
3. Upload the generated CSV files to view and analyze the data within the Streamlit interface.

## Contributing

We welcome contributions of all kinds, from bug fixes and feature additions to documentation improvements. If you're interested in contributing, please fork the repository and submit a pull request.

## License

This project is open-sourced under the MIT License. See the LICENSE file for more details.

## Acknowledgments

- Thank you to all contributors and users of StarFinder. Your support and feedback make this project possible.
- This project uses the GitHub API but is not endorsed or certified by GitHub.

---

This README provides a comprehensive overview of StarFinder, guiding users from installation to usage and contribution. It's designed to be inviting and informative, ensuring users of all levels can effectively utilize the tool.
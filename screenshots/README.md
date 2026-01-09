# Screenshots

This directory contains screenshots of all 30 LangGraph Streamlit examples.

## Generating Screenshots

To generate screenshots for any example:

1. **Run the Streamlit app:**
   ```bash
   cd Beginner/Example_01_Simple_Agent
   streamlit run app.py
   ```

2. **Take a screenshot:**
   - Use your browser's screenshot tool
   - Or use a tool like:
     - **macOS**: Cmd+Shift+4
     - **Windows**: Windows+Shift+S
     - **Linux**: Use `gnome-screenshot` or similar

3. **Save the screenshot:**
   ```bash
   # Save as screenshot.png in the example directory
   mv screenshot.png Beginner/Example_01_Simple_Agent/
   
   # Or copy to the screenshots directory
   cp screenshot.png screenshots/beginner_01_simple_agent.png
   ```

## Screenshot Naming Convention

Screenshots should be named following this pattern:
- `beginner_01_simple_agent.png`
- `advanced_05_error_handling_retry.png`
- `expert_10_enterprise_integration.png`

Format: `{level}_{number}_{example_name}.png`

## Automated Screenshot Generation

For automated screenshot generation, you can use tools like:

### Using Playwright (Python)

```python
from playwright.sync_api import sync_playwright
import subprocess
import time

def capture_screenshot(example_path, output_path):
    # Start Streamlit
    process = subprocess.Popen(['streamlit', 'run', f'{example_path}/app.py'])
    time.sleep(5)  # Wait for app to start
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:8501')
        page.wait_for_timeout(2000)
        page.screenshot(path=output_path)
        browser.close()
    
    process.terminate()

# Example usage
capture_screenshot('Beginner/Example_01_Simple_Agent', 
                  'screenshots/beginner_01_simple_agent.png')
```

### Using Selenium (Python)

```python
from selenium import webdriver
import subprocess
import time

def capture_with_selenium(example_path, output_path):
    # Start Streamlit
    process = subprocess.Popen(['streamlit', 'run', f'{example_path}/app.py'])
    time.sleep(5)
    
    driver = webdriver.Chrome()
    driver.get('http://localhost:8501')
    time.sleep(2)
    driver.save_screenshot(output_path)
    driver.quit()
    
    process.terminate()
```

## Screenshot Guidelines

When taking screenshots:

1. **Window Size**: Use a consistent viewport size (e.g., 1280x720)
2. **Content**: Show the main UI with example interaction
3. **Quality**: Use PNG format for best quality
4. **Clarity**: Ensure text is readable
5. **State**: Show the app in an interesting state (after processing input)

## TODO

- [ ] Generate screenshots for all Beginner examples (10)
- [ ] Generate screenshots for all Advanced examples (10)
- [ ] Generate screenshots for all Expert examples (10)

## Current Status

Screenshots are to be generated. Run the examples and capture screenshots following the guidelines above.

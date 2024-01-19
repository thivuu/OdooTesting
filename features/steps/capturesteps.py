import glob
import os

from behave import *
@then('I capture the screenshot')
def step_impl(context):
    # Create the capture directory if it doesn't exist
    capture_dir = os.path.join(os.path.dirname(__file__), '..', 'capture')
    os.makedirs(capture_dir, exist_ok=True)

    # Delete all existing screenshots
    screenshot_files = glob.glob(os.path.join(capture_dir, 'screenshot_*.png'))
    for file in screenshot_files:
        os.remove(file)

    # Capture the screenshot and save it to the capture directory
    feature_name = context.feature.name.replace(" ", "_")
    screenshot_path = os.path.join(capture_dir, f'{feature_name}_{context.scenario.name}_screenshot.png')
    context.driver.save_screenshot(screenshot_path)

    context.driver.close()
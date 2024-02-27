import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from selenium import webdriver
import argparse


class Handler(FileSystemEventHandler):
    """
    A class that handles file system events and triggers actions based on the event type.

    Args:
        browser (object): The browser object used to execute JavaScript code.
        extensions (list): A list of file extensions to watch for changes.

    """

    def __init__(self, browser, extensions):
        self.browser = browser
        self.extensions = extensions

    def on_modified(self, event):
        """
        Event handler method called when a file is modified.

        Args:
            event (object): The file system event object.

        """
        if any(event.src_path.endswith(ext) for ext in self.extensions):
            print(
                f"Detected change in {event.src_path}. Reloading page..."
            )
            self.browser.execute_script("""
                caches.keys().then(function(names) {
                    for (let name of names)
                        caches.delete(name);
                });
            """)
            self.browser.refresh()


def handler(browser_type, extensions, path_to_watch, url, recursive=False):
    """
    Handles the browser automation and file monitoring.

    Args:
        browser_type (str): The type of web driver to use ('firefox', 'chrome', 'edge', 'safari').
        extensions (list): List of file extensions to monitor for changes.
        path_to_watch (str): The path to the directory to monitor for file changes.
        url (str): The URL to open in the browser.
        recursive (bool, optional): Whether to monitor subdirectories recursively. Defaults to False.
    """

    match browser_type:
        case 'firefox':
            browser = webdriver.Firefox()
        case 'chrome':
            browser = webdriver.Chrome()
        case 'edge':
            browser = webdriver.Edge()
        case 'safari':
            browser = webdriver.Safari()
        case _:
            print('Driver not found')
            exit(1)

    browser.get(url)
    browser.maximize_window()

    print('Browser started')
    print('Press Ctrl+C to stop')

    event_handler = Handler(browser, extensions)
    observer = Observer()
    observer.schedule(event_handler, path=path_to_watch, recursive=recursive)
    observer.start()

    print('Watching for changes in ' + path_to_watch)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

    # Fecha o navegador ao encerrar o script
    browser.quit()


def main():
    """
    Watch for changes in a folder and reload the page when a file is modified.

    Args:
        --browser, -b: Browser type. Choices: ['firefox', 'chrome', 'edge', 'safari'].
        --path, -p: Path to folder to watch for changes.
        --url, -u: Page url to open in browser.
        --extensions, -e: Extensions to watch for changes.
        --recursive, -r: Watch subfolders recursively.
    """
    parser = argparse.ArgumentParser(
        description=
        'Watch for changes in a folder and reload the page when a file is modified.'
    )
    parser.add_argument(
        '--browser',
        '-b',
        type=str,
        help='Browser type',
        choices=['firefox', 'chrome', 'edge', 'safari'],
        required=True,
    )
    parser.add_argument(
        '--path',
        '-p',
        metavar='PATH_TO_WATCH',
        type=str,
        help='Path to folder to watch for changes',
        required=True,
    )
    parser.add_argument(
        '--url',
        '-u',
        metavar='PAGE_URL',
        type=str,
        help='Page url to open in browser',
        required=True,
    )
    parser.add_argument(
        '--extensions',
        '-e',
        metavar='EXTENSIONS',
        type=str,
        help='Extensions to watch for changes',
        nargs='+',
        required=True,
    )
    parser.add_argument(
        '--recursive',
        '-r',
        action='store_true',
        help='Watch subfolders recursively',
    )
    args = parser.parse_args()
    print('Handler starting ...')
    handler(browser_type=args.browser,
            extensions=args.extensions,
            path_to_watch=args.path,
            url=args.url,
            recursive=args.recursive)
    print('Handler finished')


if __name__ == "__main__":
    main()

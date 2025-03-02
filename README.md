# Hoarder Plugin

Hoarder is a FlowLauncher plugin that allows you to search for bookmarks stored in the Hoarder application. This plugin provides a quick and easy way to access your saved bookmarks directly from the FlowLauncher interface.

## Installation

You can install this plugin via the FlowLauncher plugin manager with the following command:

```
pm install Hoarder
```

## Configuration

Before you can use this plugin, you will need to configure it with your local Hoarder instance's base URL and API key. You can do this by setting the following two values in the plugin's settings:

- `Hoarder Base Address`: This is the base URL of your local Hoarder instance. For example, if you run Hoarder on http://localhost:8080, then this should be set to `http://localhost:8080`.

- `Hoarder API Key`: This is the API key that allows the plugin to access your Hoarder bookmarks. You can obtain this key from the Hoarder web interface by going to your profile settings > User Settings > API Keys page and clicking on "New API Key".

## Usage

Once installed, you can activate the Hoarder plugin by using the action keyword `ho`. Simply type `ho` followed by your search query to find matching bookmarks stored in Hoarder.

### Example

To search for a bookmark related to "Python", you would use the following command in FlowLauncher:

```
ho Python
```

## Features

- **Quick Search**: Instantly search through your Hoarder bookmarks.
- **Easy Access**: Open bookmarks directly from FlowLauncher.
- **Context Menu**: Access additional options using the context menu.

## Context Menu

The plugin provides a context menu option:

- **Copy URL to clipboard**: Copies the URL of the selected item to the clipboard

## Development

This plugin is developed using Python and leverages the FlowLauncher API to integrate seamlessly with the FlowLauncher platform.

## Author

Hoarder Plugin is developed by Robert Verdam. You can find more about this plugin and contribute to its development on [GitHub](https://github.com/rverdam/Flow.Launcher.Plugin.Hoarder).

## License

This project is licensed under the MIT License.

---

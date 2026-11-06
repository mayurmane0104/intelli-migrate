# Configuring Command Autocompletion | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/exchange/apicat-configure-cli-autocomplete](https://docs.mulesoft.com/exchange/apicat-configure-cli-autocomplete)

---

1) Add the autocomplete env var to your bash profile and source it $ printf "eval $(api-catalog autocomplete:script bash)" >> ~/.bashrc; source ~/.bashrc NOTE: If your terminal starts as a login shell you may need to print the init script into ~/.bash_profile or ~/.profile. 2) Test it out, e.g.: $ api-catalog <TAB><TAB> # Command completion $ api-catalog [command] --<TAB><TAB> # Flag completion

# Configuring Command Autocompletion

The `api-catalog-cli autocomplete` command enables you to configure completion for API Catalog CLI commands.

To configure command autocompletion:

- 
If you are using a Bash shell: - 
Run `api-catalog autocomplete bash`. This creates a cache and displays configuration and test instructions.
- 
Follow the instructions that are displayed by the command: 
 
- 
- 
If you are using a Z shell: - 
Run `api-catalog autocomplete zsh`. This creates a cache and displays configuration and test instructions.
- 
Follow the instructions that are displayed by the command: 1) Add the autocomplete env var to your zsh profile and source it $ printf "eval $(api-catalog autocomplete:script zsh)" >> ~/.zshrc; source ~/.zshrc NOTE: After sourcing, you can run `$ compaudit -D` to ensure that no permissions conflicts are present 2) Test it out, e.g.: $ api-catalog <TAB> # Command completion $ api-catalog [command] --<TAB> # Flag completion 
 
- 

## api-catalog autocomplete

$ api-catalog autocomplete [flags]

This command accepts the following flags:

| Flag | Description | 
|---|---|
| blank | Displays instructions for configuring autocompletion | 
| bash | Installs autocompletion using Bash shell settings | 
| zsh | Installs autocompletion using Z shell settings | 
| -r, --refresh cache | Removes the current autocompletion configuration. Use this before running the command with a different shell type. | 

**Examples**

$ api-catalog autocomplete $ api-catalog autocomplete bash $ api-catalog autocomplete zsh $ api-catalog autocomplete --refresh-cache

| The API Catalog CLI autocomplete plugin is not currently supported in Windows. |
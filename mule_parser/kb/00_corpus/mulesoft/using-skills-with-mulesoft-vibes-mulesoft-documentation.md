# Using Skills with MuleSoft Vibes | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/vibes-skills](https://docs.mulesoft.com/anypoint-code-builder/vibes-skills)

---

# Using Skills with MuleSoft Vibes

Skills are reusable instruction sets that MuleSoft Vibes activates only when they apply to your task. Each skill packages guidance and optional resources so MuleSoft Vibes can follow a consistent workflow without loading that material for unrelated messages.

When your request matches a skill’s description, MuleSoft Vibes uses the `use_skill` tool to load the full instructions and run them for that task. Unlike workspace rules that stay active across conversations, skills load as needed, which leaves more context available for other work.

MuleSoft publishes Mule development skills from the `mulesoft-dx` repository as the `@salesforce/mulesoft-vibes-skills` package so you can use them across agents such as MuleSoft Vibes, Claude Code, Cursor, Cline, and Codex.

**Default skills** are preloaded in MuleSoft Vibes and enabled by default. You can turn on and off each default skill individually.
**Workspace skills** are available only in the workspace or project where they’re defined.
**Global skills** are available in every project and workspace.

## Manage Default Skills in MuleSoft Vibes

Default skills are available automatically when you use MuleSoft Vibes where the feature is supported.

Use MuleSoft Vibes settings to turn on and off each default skill based on your workflow.

## Set Up Skills in Your Project

To add **workspace skills** to a project, add skills under `.a4drules/skills/` in your workspace. Each skill is a directory whose name matches the skill. The directory contains a `SKILL.md` file with the instructions (and optional YAML frontmatter for metadata). You can add supporting material in subfolders such as `references/`, `assets/`, or `scripts/` inside that skill directory.

Commit `.a4drules/skills/` with your project so everyone who uses the repository gets the same skills.

## Install MuleSoft Skills in Claude Code

These steps are written for Claude Code and also apply to other supported agents that use the same installer flow.

Before you install skills, create a connected app and authenticate Anypoint CLI:

- 
`anypoint-cli-v4 conf client_id {myClientID}`
- 
`anypoint-cli-v4 conf client_secret {myClientSecret}`For more information, see [Authentication to the Anypoint Platform CLI](../anypoint-cli/latest/auth).

To install MuleSoft skills:

- 
Make sure Node.js is installed. 
- 
Install the `anypoint-cli-dx-mule-plugin`.
- 
Run: `npx skills add mulesoft/mulesoft-dx/skills/mule-development`
- 
Select the skills you want to install. 
- 
Select the agent targets for the installation: - 
Keep **Universal (**selected. It is always included by the installer.`.agents/skills`)
- 
Select **Claude Code (**under`.claude/skills`)**Additional agents**.
 
- 
- 
Select a scope: - 
**Project**installs in the current directory so you can commit the skills with your project.
- 
**Global**makes the skills available to all instances of supported agents.
 
- 
- 
Select an installation method: - 
**Symlink (Recommended)**installs one shared copy for all selected agent types.
- 
**Copy to all agents**installs independent copies for each selected agent type.
 
- 
- 
Confirm the installation by typing `yes`.

| Use `mulesoft/mulesoft-dx/skills/mule-development`in the`install`command. The shorter`mulesoft/mulesoft-dx`path doesn’t resolve the nested skills directory. | 

## MuleSoft Skills Catalog

The default MuleSoft skills set includes:

| Skill Name | Description | 
|---|---|
| 
 | Run Anypoint Code Builder system diagnostics, including RAM, CPU, IOPS, and Windows optimizations. | 
| 
 | Configure and implement Mule secure properties to encrypt sensitive data. | 
| 
 | Add or update  | 
| 
 | Create a new Anypoint Code Builder run configuration. | 
| 
 | Delete an existing Anypoint Code Builder run configuration. | 
| 
 | Edit an existing Anypoint Code Builder run configuration. | 
| 
 | Run or debug a Mule application by using an existing Anypoint Code Builder run configuration. | 
| 
 | Create, update, or fix a Mule flow, subflow, or component. This skill runs a validation script at startup to check whether  | 
| 
 | Generate MuleSoft projects from Exchange templates or from scratch. | 

## Skills and MCP Tools

Model Context Protocol (MCP) servers expose **tools** that perform actions, such as generating a flow or calling an API. **Skills** supply structured instructions and workflows the assistant follows when a task matches the skill. You typically use both: tools carry out operations, while skills guide how and when to apply them for specific scenarios.

For configuring MCP servers in Anypoint Code Builder, see [Configuring an MCP Server](vibes-mcp-server).
# Search for code, issues, projects, and users in CodeCatalyst - Amazon CodeCatalyst

**Source:** [https://docs.aws.amazon.com/codecatalyst/latest/userguide/search](https://docs.aws.amazon.com/codecatalyst/latest/userguide/search)

---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](./migration.html).

Use the search bar or a dedicated search results window in CodeCatalyst to search through code, issues, projects, and users CodeCatalyst.

You can find resources across your space and projects by entering queries such as name, description, and status into the search bar. You can also refine your search queries using the search query language.

###### To search

- 
   In the search bar in the top navigation bar, enter a search query. 
- 
   (Optional) Refine your search query using CodeCatalyst's search query language. For more information, see [Refining your search query](#search-query-language-examples).
- 
   Do one of the following: - 
     To search for resources within the project that you are currently in, choose **This project**.
- 
     To search for resources within all of the projects in the space you are currently in, choose **This space**.
 
- 
     
- 
   View search results in a dedicated search results window by doing one of the following: - 
     In the bottom of the quick search results window, choose **View all results in project-name | space-name**to view all search results.
- 
     Press **Enter**to view all search results.
 
- 
     

###### Tip

Mention other project users in a pull request comment or description, or in an issue comment or description, by using the @ sign followed by their display name or user name. You can also link to resources like issues or code files by using the @ sign followed by the name of the issue or code file.

## Refining your search query

  If you can't find what you're looking for after searching, you can refine your search with CodeCatalyst's specialized query language. Individual fields have no character limit, but the overall query has a limit of 1,024 characters.

### Refining by type

To refine the scope of your search to a specific type of information, include
    `type:result-type``result-type` is `code`, `issue`, `project`, or
    `user` .

Examples:

- 
     `type:code AND java`– Show code results in code-related fields that contain “java”.For more information, see [Code fields](#search-query-language-type-code).
- 
     `type:issue AND Bug`– Show issue results in issue-related fields that contain “Bug”.For more information, see [Issue fields](#search-query-language-type-issue).
- 
     `type:user AND MaryMajor`– Show user results in user-related fields that contain “MaryMajor”.For more information, see [User fields](#search-query-language-type-user).
- 
     `type:project AND Datafeeder`– Show project results that contain "Datafeeder".For more information, see [Project fields](#search-query-language-type-project).

### Refining by field

To refine the scope of your search to a specific field, include
      `field-name:query``field-name` is `title`, `username`,
     `project`, `description`, and so on, and `query`
    is the text for which you are searching. For a list of fields, see [Searchable fields reference](#search-query-language-searchable-fields). You can search for multiple queries
    using parentheses.

Examples:

- 
     `title:bug`– Show results where the title contains “bug”.
- 
     `username:John`– Show results where the user name contains “John”.
- 
     `project:DataFeeder`– Show results in the project “DataFeeder”. Query isn't case sensitive.
- 
     `description:overview`– Show results where the description contains “overview”.

### Refining with Boolean operators

To specify constraints on search phrases, you can use the Boolean operators
     `AND`, `OR`, and `NOT`.  If you list multiple phrases, CodeCatalyst
    joins them with `OR` by default. You can group search phrases using
    parentheses.

- 
     `exception AND type:code`– Show only code results for “exception”.
- 
     `path:README.md AND repo:ServerlessAPI`– Show results for paths with “README.md” where the repository is named “ServerlessAPI”.
- 
     `buildspec.yml AND (repo:ServerlessAPI OR ServerlessWebApp)`– Show results for “buildspec.yml” where the repository is “ServerlessAPI” or “ServerlessWebApp”.
- 
     `path:java NOT (path:py OR path:ts)`– Show results where the path contains “java” but not “py” or “ts”.

### Refining by project

To refine the scope of your search to a specific project, include 
   `project:name AND query``name` is the project within which you are searching and 
   `query` is the content for which you are searching.

- 
  `project:name AND query`– Show results where the path contains the query and the project name.

## Considerations when working with search

  **Delayed content updates** – It can take several
   minutes for content updates, such as name changes or issue reassignments, to be reflected in the
   search results. Large updates, such as a code base migration, can take longer to appear in search
   results.

**Escaping special characters** – The following special 
   characters require special consideration in your search queries: ```
+ - & & || ! ( ) { } [ ] 
    ^ " ~ * ? : \
```
. Special characters will not influence the query, and you must either remove 
   them or escape them. To escape a character, add a backslash (\) in front of it. For example, the 
   search query [Feature] should either be Feature or \[Feature\].

**Narrowing search** – Search isn't case sensitive.
   Searching in all lowercase prevents your queries from splitting up words on case change. For
   example, to query for `MyService` and only `MyService`, consider querying
    `myservice` to avoid results that contain only `my` or
    `service`.

Search joins words and parts of words with OR-wise conjunction by default. For example,
    `new function` could return results containing both `new` and
    `function` and also results with only `new` or `function`. To
   avoid the latter, combine multiple words with `AND`. For example, you can search
    `new AND function`.

**Default branches** – Search will only return code results 
   from the latest commit on a source repository’s default branch. To find code on other branches or 
   commits, consider [cloning the repository locally](./source-repositories-clone.html), 
   [opening the branch in a Dev Environment](./devenvironment-create.html), or 
   [viewing the branches and details in the CodeCatalyst UI](./source-branches-view.html). 
   Changing the default branch results in updates to the files discoverable by search. For more information, 
   see [Managing the default branch for a repository](./source-branches-default-branch.html).

###### Important

CodeCatalyst doesn't support detecting changes in the default branch for linked 
            repositories. To change the default branch for a linked repository, you must first unlink it 
            from CodeCatalyst, change the default branch, and then link it again. For more information, 
            see [Linking GitHub repositories, Bitbucket repositories, GitLab project repositories, and Jira projects in CodeCatalyst](./extensions-link.html).

As a best practice, always make sure you have the latest version of the extension before you link a repository.

## Searchable fields reference

  CodeCatalyst searches the following fields when you enter search queries. Aliases are another name that you can use to reference the field in the advanced query language.

| Field | Alias | Description | 
|---|---|---|
| branchName | branch | Name of branch the code file is on. | 
| code | N/A | Information about the code contents in the form of code snippets indicating parts of the source code that matched the search. | 
| commitId | N/A | Commit ID of the commit in which the returned code ﬁle was last updated. May or may
         not be the commit ID at the tip of the branch name speciﬁed in  | 
| commitMessage | N/A | Commit message of the commit in which the code ﬁle was last updated. May or may
         not be the commit message at the tip of the branch name speciﬁed in  | 
| filePath | path | File path of this code file. | 
| lastUpdatedBy | N/A | CodeCatalyst user who last updated the code ﬁle. If the user name isn't available, this value will be the email address of the user as conﬁgured in the Git conﬁguration ﬁle. | 
| lastUpdatedById | N/A | System-generated unique ID of user that last updated the code ﬁle. If the user ID isn't available, this value might be the email address of the user. | 
| lastUpdatedTime | N/A | Time when the search data was last updated with the commit that contained the code ﬁle (in coordinated universal time (UTC) timestamp). | 
| projectId | N/A | System-generated unique ID of the project. | 
| projectName | projectNames, project | Display name of the project that contains the source repository where the code ﬁle has been committed. | 
| repositoryId | repoId | System-generated unique ID of the source repository. | 
| repositoryName | repository, repo | Display name of the source repository where the code ﬁle has been committed. | 

| Field | Alias | Description | 
|---|---|---|
| assigneeIds | assigneeId | System-generated unique IDs of the users assigned to the issue. | 
| assignees | assignee | User names of the users assigned to the issue. | 
| createdBy | N/A | Display name of the user who created the issue. | 
| createdById | N/A | System-generated unique ID of the user who created the issue. | 
| createdTime | N/A | Time the issue was created (in coordinated universal time (UTC) timestamp). | 
| description | N/A | Description of the issue. | 
| isArchived | archived | Boolean value that indicates whether to create the issue in an archived state. | 
| isBlocked | blocked | Boolean value that indicates whether the issue is marked as blocked. | 
| labelIds | labelId | System-generated unique IDs of the labels for an issue. | 
| lastUpdatedBy | N/A | Display name of use who last updated the issue. | 
| lastUpdatedById | N/A | System-generated unique ID of the user who last updated the issue. | 
| lastUpdatedTime | N/A | Time the issue was last updated (in coordinated universal time (UTC) timestamp). | 
| priority | N/A | Priority of the issue, if one has been assigned. | 
| projectId | N/A | System-generated unique ID of the project. | 
| projectName | projectNames, project | Project in which this issue can be found. | 
| shortId | N/A | Shortened, auto-incrementing identifier for the issue. | 
| status | N/A | Status of the issue that indicates if issue is in backlog or column on board. | 
| statusId | N/A | System identifier of the status. | 
| title | N/A | Title of the issue. | 

| Field | Alias | Description | 
|---|---|---|
| description | N/A | Description of the project. | 
| lastUpdatedTime | N/A | Time when the project metadata was last updated (in coordinated universal time (UTC) timestamp). | 
| projectName | project | Name of the project in the space. | 
| projectPath | N/A | URL-routable name of the project, deﬁned during project creation. Used in URLs that require the project name. | 

| Field | Alias | Description | 
|---|---|---|
| displayName | N/A | Name used for the user in CodeCatalyst. Display names are not unique. | 
|  | N/A | Email address of the user. | 
| lastUpdatedTime | N/A | Time when the user metadata was last updated (in coordinated universal time (UTC) timestamp). | 
| userName | username | User name chosen by the user when they signed up for CodeCatalyst. Unlike display names, user names can't be changed. |
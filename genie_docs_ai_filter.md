# Databricks Genie:  setup, natural language querying, trusted assets, and administration, monitoring, agents, capabilities

*Scraped 8 pages on 2026-03-23 04:45*

---

## Table of Contents

1. [Agent mode in Genie spaces](https://docs.databricks.com/aws/en/genie/agent-mode)
2. [Monitor Genie spaces usage with audit logs and alerts](https://docs.databricks.com/aws/en/ai-bi/admin/audit)
3. [Set up and manage a Genie space](https://docs.databricks.com/aws/en/genie/set-up)
4. [Build a knowledge store for more reliable Genie spaces](https://docs.databricks.com/aws/en/genie/knowledge-store)
5. [Use parameters in SQL queries](https://docs.databricks.com/aws/en/genie/query-params)
6. [Use trusted assets in Genie spaces](https://docs.databricks.com/aws/en/genie/trusted-assets)
7. [Use benchmarks in a Genie space](https://docs.databricks.com/aws/en/genie/benchmarks)
8. [Curate an effective Genie space](https://docs.databricks.com/aws/en/genie/best-practices)

================================================================================

## 1. Agent mode in Genie spaces

**URL:** https://docs.databricks.com/aws/en/genie/agent-mode
**Crawl depth:** 0

---

* * [Business intelligence](/aws/en/ai-bi/)* [Genie spaces](/aws/en/genie/)* Agent mode

On this page

Last updated on **Mar 18, 2026**

# Agent mode in Genie spaces

note

Agent mode was formerly known as Research Agent.

Agent mode extends Genie's capabilities to answer both straightforward data questions and complex business questions. It uses multi-step reasoning and hypothesis testing to uncover deeper insights. When you ask a question, Agent mode creates and refines a research plan, running multiple SQL queries, learning from each result, and iterating until it has enough evidence to provide a comprehensive answer.

Unlike standard Genie queries, Agent mode:

* **Creates research plans**: Develops a structured approach and hypotheses for answering complex questions.
* **Runs multiple queries**: Executes several SQL queries to gather evidence from different angles.
* **Learns and iterates**: Continuously adjusts its approach based on what it discovers, refining its reasoning until it's confident in the answer.
* **Delivers comprehensive reports**: Provides detailed summaries with citations, visualizations, and supporting tables.

Agent mode is designed for both complex, exploratory questions and straightforward data questions like:

* What are our top-selling products this quarter?
* What customer segments are most profitable?
* Why did revenue spike in June 2025?
* How can we reduce order cancellations this holiday season?
* What factors contributed to customer churn last quarter?
* Which marketing campaigns had the best ROI and why?

## Requirements and availability[â](#requirements-and-availability "Direct link to Requirements and availability")

Agent mode is in [Public Preview](/aws/en/release-notes/release-types). Workspace admins control access using the previews page. See  [Manage workspace-level previews](/aws/en/admin/workspace-settings/manage-previews#workspace).

To use Agent mode, your workspace must meet the following criteria.

### Have a well-prepared Genie space[â](#have-a-well-prepared-genie-space "Direct link to Have a well-prepared Genie space")

Agent mode relies heavily on the context within your Genie space to reason about your data. You must meet all requirements for setting up a Genie space. See [Set up a Genie space](/aws/en/genie/#setup-permissions).

To optimize your Genie space for Agent mode, follow the comprehensive guidance in:

* [Set up and manage a Genie space](/aws/en/genie/set-up): Initial setup and configuration
* [Curate an effective Genie space](/aws/en/genie/best-practices): Best practices for setting up an effective Genie space
* [Build a knowledge store for more reliable Genie spaces](/aws/en/genie/knowledge-store): Adding space-specific context

### Regional availability[â](#regional-availability "Direct link to Regional availability")

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Region Availability|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | Americas & Europe workspaces Available (cross-Geo not required)|  |  |  |  | | --- | --- | --- | --- | | Australia, New Zealand, and Japan workspaces Available (cross-Geo not required)|  |  | | --- | --- | | All other regions Available only if cross-Geo is enabled. See [Enable cross-Geo processing](/aws/en/resources/databricks-geos#cross-geo-processing). | | | | | | | |

## Manage Agent mode[â](#manage-agent-mode "Direct link to Manage Agent mode")

Workspace admins can control access to **Genie Agent mode (Public Preview)** using the previews page. See  [Manage workspace-level previews](/aws/en/admin/workspace-settings/manage-previews#workspace).

After Agent mode is enabled, it is available for all Genie spaces within that workspace. All users with access to a Genie space can use Agent mode. All requirements for accessing a Genie space and its data apply. See [Set up a Genie space](/aws/en/genie/#setup-permissions).

## Use Agent mode[â](#use-agent-mode "Direct link to Use Agent mode")

To ask questions using Agent mode:

1. Open a Genie space.
2. Click  the Agent mode icon in the chat box.
3. Enter a question and send your prompt. Agent mode begins its research and may ask follow-up questions to clarify your intent. Agent mode responses may take longer to generate than standard Genie space responses. When complete, it answers with a final report containing specific findings, visualizations, and citations to research steps.
4. After the report is generated, you can send additional clarification prompts to refine your report or generate new reports on different research questions. You can provide feedback to help improve Agent mode.

## Export Agent mode reports[â](#export-agent-mode-reports "Direct link to export-agent-mode-reports")

You can export Agent mode reports as PDF files for sharing or offline review. After Agent mode completes a report, click  **Download PDF** at the bottom right of the report to download it, including findings, visualizations, and citations.

## What questions can Agent mode answer?[â](#what-questions-can-agent-mode-answer "Direct link to What questions can Agent mode answer?")

Agent mode performs best when you ask specific, data-driven questions about your business data. It handles both straightforward queries and complex questions that need multi-step reasoning, such as:

* Why did revenue spike in June 2025?
* What are our top-selling products this quarter?
* How can we reduce the number of order cancellations this holiday season?
* Tell me how our new product is doing in EMEA
* What customer segments are most profitable?
* What factors contributed to customer churn last quarter?
* Which marketing campaigns had the best ROI and why?

## Frequently asked questions[â](#frequently-asked-questions "Direct link to Frequently asked questions")

### Are there additional costs for Agent mode while in Public Preview?[â](#are-there-additional-costs-for-agent-mode-while-in-public-preview "Direct link to Are there additional costs for Agent mode while in Public Preview?")

No. During the Public Preview period, Agent mode does not have additional costs beyond the standard warehouse compute costs associated with running SQL queries.

### Does Agent mode use different data than standard Genie?[â](#does-agent-mode-use-different-data-than-standard-genie "Direct link to Does Agent mode use different data than standard Genie?")

No. Agent mode uses the same context and data as the standard Genie experience. To learn about the context that Genie uses to generate responses, see  [How does Genie generate a response?](/aws/en/genie/#response-generation) and [Privacy and security](/aws/en/genie/#privacy-security).

### Is Agent mode available through the API?[â](#is-agent-mode-available-through-the-api "Direct link to Is Agent mode available through the API?")

No. During the Public Preview period, users can only submit Agent mode prompts through the Databricks UI.

### What models power Agent mode?[â](#what-models-power-agent-mode "Direct link to What models power Agent mode?")

Agent mode uses Sonnet models. Genie is a managed service that continuously evaluates models from multiple providers and uses the most performant and accurate options. For more information, see [Databricks AI assistive features trust and safety](/aws/en/databricks-ai/databricks-ai-trust).

### How do I provide feedback on Agent mode?[â](#how-do-i-provide-feedback-on-agent-mode "Direct link to How do I provide feedback on Agent mode?")

Share feedback with your Databricks account team. In particular, Databricks is seeking feedback in the following areas:

* **Research steps**: Whether Agent mode investigates the right dimensions and generates accurate SQL.
* **Answer summaries**: Preferences for format, level of detail, and clarity.
* **Usability**: Any challenges in finding, enabling, or using the feature.
* **Context handling**: Whether Agent mode uses relevant context effectively.
* **Success stories**: Examples where Agent mode delivered valuable insights.

* [Requirements and availability](#requirements-and-availability)
  + [Have a well-prepared Genie space](#have-a-well-prepared-genie-space)+ [Regional availability](#regional-availability)* [Manage Agent mode](#manage-agent-mode)* [Use Agent mode](#use-agent-mode)* [Export Agent mode reports](#export-agent-mode-reports)* [What questions can Agent mode answer?](#what-questions-can-agent-mode-answer)* [Frequently asked questions](#frequently-asked-questions)
            + [Are there additional costs for Agent mode while in Public Preview?](#are-there-additional-costs-for-agent-mode-while-in-public-preview)+ [Does Agent mode use different data than standard Genie?](#does-agent-mode-use-different-data-than-standard-genie)+ [Is Agent mode available through the API?](#is-agent-mode-available-through-the-api)+ [What models power Agent mode?](#what-models-power-agent-mode)+ [How do I provide feedback on Agent mode?](#how-do-i-provide-feedback-on-agent-mode)


================================================================================

## 2. Monitor Genie spaces usage with audit logs and alerts

**URL:** https://docs.databricks.com/aws/en/ai-bi/admin/audit
**Crawl depth:** 0

---

* * [Business intelligence](/aws/en/ai-bi/)* [Genie spaces](/aws/en/genie/)* Monitor usage

On this page

Last updated on **Feb 25, 2026**

# Monitor Genie spaces usage with audit logs and alerts

Preview

This feature is in [Public Preview](/aws/en/release-notes/release-types).

warning

Due to an outage, some dashboard audit logs might be missing for the period October 16, 2025 â November 19, 2025.

This page has sample queries that workspace admins can use to monitor activity associated with Genie spaces. All queries access the audit logs table, which is a system table that stores records for all audit events from workspaces in your region.

See [Monitor account activity with system tables](/aws/en/admin/system-tables/). For a comprehensive reference of available audit log services and events, see [Audit log reference](/aws/en/admin/account-settings/audit-logs).

note

For information about monitoring dashboard usage, see [Monitor dashboard usage](/aws/en/dashboards/monitor-usage).

## Track Genie space interactions[â](#track-genie-space-interactions "Direct link to track-genie-space-interactions")

The examples in this section demonstrate how to retrieve audit logs for common questions about Genie space activity.

### Query for feedback[â](#query-for-feedback "Direct link to query-for-feedback")

The following query returns [feedback ratings](/aws/en/genie/set-up#response-feedback) submitted for the Genie spaces in your workspace from the past 30 days. The columns in the query include the `space_id` and the email address of the user who submitted the feedback, along with all other columns from the system table.

SQL

```
SELECT
  user_identity.email as user_email,
  action_name,
  request_params.space_id,
  request_params.feedback_rating,
  *
FROM
  system.access.audit
WHERE
  service_name = 'aibiGenie'
  AND action_name = 'updateConversationMessageFeedback'
  AND event_date >= current_date() - interval 30 days
```

### Return requests for review[â](#return-requests-for-review "Direct link to return-requests-for-review")

The following query returns [request for review](/aws/en/genie/set-up#response-feedback) activity from Genie spaces over the past 30 days. It includes the `space_id`, the email address of the user who added the comment, the type of action, and all other columns from the source table.

SQL

```
SELECT
  user_identity.email as user_email,
  action_name,
  request_params.space_id,
  *
FROM
  system.access.audit
WHERE
    service_name = 'aibiGenie'
    AND action_name = 'createConversationMessageComment'
    AND event_date >= current_date() - interval 30 days
```

### API response codes[â](#api-response-codes "Direct link to api-response-codes")

The following query returns a count of Genie API requests grouped by HTTP response status code for the past 30 days. Use it to monitor success rates, spot errors (such as 429 or 5xx), and track activity for conversation start and create message actions. Results include the date and time to the minute so you can correlate 429 rate-limit responses with request volume per minute (for example, more than 5 requests in a minute).

SQL

```
SELECT
  date_trunc('minute', event_time) as event_minute,
  response.status_code,
  COUNT(*) as request_count
FROM
  system.access.audit
WHERE
  service_name = 'aibiGenie'
  AND action_name IN ('genieStartConversationMessage', 'genieCreateConversationMessage')
  AND event_date >= current_date() - interval 30 days
GROUP BY
  date_trunc('minute', event_time),
  response.status_code
ORDER BY
  event_minute,
  response.status_code
```

## Set up alerts[â](#set-up-alerts "Direct link to Set up alerts")

You can set alerts to automate this type of monitoring. See [Create an alert](/aws/en/sql/user/alerts/#create-alert) to learn how to set an alert on a specific threshold.

* [Track Genie space interactions](#track-genie-space-interactions)
  + [Query for feedback](#query-for-feedback)+ [Return requests for review](#return-requests-for-review)+ [API response codes](#api-response-codes)* [Set up alerts](#set-up-alerts)


================================================================================

## 3. Set up and manage a Genie space

**URL:** https://docs.databricks.com/aws/en/genie/set-up
**Crawl depth:** 0

---

* * [Business intelligence](/aws/en/ai-bi/)* [Genie spaces](/aws/en/genie/)* For space authors* Set up a Genie space

On this page

Last updated on **Mar 18, 2026**

# Set up and manage a Genie space

This article explains how to set up and manage a Genie space, a chat interface for business users to ask natural-language questions about their data.

## Technical requirements and limits[â](#technical-requirements-and-limits "Direct link to technical-requirements-and-limits")

The following requirements and limits apply when using Genie spaces:

* **Unity Catalog:** The data for the Genie space must be registered to Unity Catalog. You can add up to 30 tables or views to a Genie space.
* **Compute:** Genie spaces require a pro or serverless SQL warehouse. When you create or configure a Genie space, you must have at least CAN USE permission on the selected warehouse. Your compute credentials are embedded into the Genie space and used to process all queries for all users.
* **Throughput:** Each workspace can handle up to 20 questions per minute across all Genie spaces when accessed though the Databricks UI. When accessing Genie spaces using the [Genie API](https://docs.databricks.com/api/workspace/genie) free tier (Public Preview), throughput is limited to a best effort five questions per minute per workspace, across all Genie spaces. These default limits are in place to prevent abuse. To scale beyond, please contact your Databricks account team.
* **Capacity:** Each Genie space can support up to 10,000 conversations, and each conversation can include up to 10,000 messages.

## Required permissions[â](#required-permissions "Direct link to Required permissions")

To create or edit a Genie space, you must have the following permissions and entitlements:

* **Entitlements:** You must have the Databricks SQL workspace entitlement. See [Manage entitlements](/aws/en/security/auth/entitlements).
* **Compute:** CAN USE access on at least one pro or serverless SQL warehouse.
* **Data access:** `SELECT` privileges on the data used in the space.
* **Genie space ACLs:** At least CAN EDIT permissions on the Genie space. Genie space creators automatically have CAN MANAGE permissions on spaces they create. See [Genie space ACLs](/aws/en/security/auth/access-control/#genie-space-acls).

note

Configuring data and compute access requires elevated permissions, generally restricted to an administrator. See [Create a SQL warehouse](/aws/en/compute/sql-warehouse/create) and [Manage privileges in Unity Catalog](/aws/en/data-governance/unity-catalog/manage-privileges/).

## Manage Genie access[â](#manage-genie-access "Direct link to manage-genie-access")

Genie uses partner-powered AI features, which must be enabled at the account and workspace levels. To learn how to manage these features for your account, see [Partner-powered AI features](/aws/en/databricks-ai/partner-powered).

note

You must be an account administrator to manage access to this feature. If you disable [Partner-powered AI features](/aws/en/databricks-ai/partner-powered), users with the Databricks SQL entitlement can still click the **Genie** icon in the sidebar, but they cannot access any Genie spaces.

## Create a Genie space[â](#-create-a-genie-space "Direct link to -create-a-genie-space")

To create a Genie space:

1. Click **Genie** in the sidebar.
2. Click **New** in the upper-right corner of the screen.
3. Choose the data sources that you want to include in your Genie space. Then, click **Create**.

Before sharing the space with users, Databricks recommends building a knowledge store and adding example SQL queries and instructions to improve response accuracy. The sections below walk you through each configuration option.

## Review query suggestions[â](#review-query-suggestions "Direct link to review-query-suggestions")

To learn about your space's data, Genie accesses information in your workspace to better understand relationships between tables and your business semantics. When you add data assets to a space, Genie automatically searches for relevant popular workspace queries associated with those assets. Your user credentials are used to find relevant queries for which you have at least CAN VIEW permissions. If the search returns queries, a notification appears in the **Data** tab of the **Instructions** panel. Click **Review** to see the suggested queries.

For more information about query access permissions, see [Query ACLs](/aws/en/security/auth/access-control/#query).

Use the **Review Suggested Queries** dialog to review, edit, accept, or reject the suggested queries. Other users with at least CAN EDIT access on the Genie space can review queries, provided they have at least CAN VIEW access on the query itself.

1. The **Title** text is prepopulated with a question. Revise or edit the question by typing in the **Title** field.
2. The **Code** field contains the complete text of the suggested SQL query. This field is not editable. To view the full query, click **... more lines**.
3. If you have sufficient permissions on the query, you can click **SQL query** to open the query in the **Query history** UI. See [View query history](/aws/en/sql/user/queries/query-history#view-history).
4. After you determine whether the query is relevant for your space, click **Accept** or **Reject** to add it to your space or dismiss the suggestion accordingly.
5. Click the other suggestions to expand and review.

Accepted queries appear in the **SQL Queries** context for the space. After they are added to the space, the suggested queries and associated questions are fully editable. See  [Add example SQL queries and functions](#example-queries).

If no suggested queries are returned:

* You might not have sufficient access to relevant queries.
* There might be no relevant data. If queries have not run on your included tables, the search might not return results.
* Queries irrelevant to the Genie space are not considered. For example, queries that only perform basic write operations on the included assets are not considered relevant examples for Genie.
* Genie does not suggest queries on tables that are not added to the space. If youâve created joined tables or views specifically for the Genie space, but relevant Databricks SQL queries typically run against a different source table, Genie does not return those queries in the results.

## Manage data objects[â](#-manage-data-objects "Direct link to -manage-data-objects")

To manage which data objects are included in a Genie space, click **Configure** > **Data**. Click the **Add** button to add more tables. Click the  to the right of the table name to remove a table from the space.

To view details about a data object, click the object name. The data object view shows two tabs:

* **Overview**: Shows the columns in the data object, including column names, data types, and descriptions.
* **Sample data**: Shows sample data from the table to help you understand the context and content of the data.

note

Genie can query tables beyond those explicitly added to a space. Access is controlled by Unity Catalog permissions, not by the Genie space itself. While Genie uses the attached tables and views by default, users can query other tables by prompting for joins or editing SQL directly. Similarly, if instructions or metadata reference tables outside the space, Genie can include them in generated queries.

## Build a knowledge store[â](#build-a-knowledge-store "Direct link to build-a-knowledge-store")

A knowledge store is a collection of curated semantic definitions that improves Genieâs understanding of your data and increases response accuracy. All knowledge store configurations are scoped to your Genie space and do not affect Unity Catalog metadata or other Databricks assets. See [Build a knowledge store for more reliable Genie spaces](/aws/en/genie/knowledge-store) for full details. The knowledge store includes the following:

* **Metadata customization**: Add space-specific table and column descriptions, and define synonyms that map business terms to column names. See  [View columns](/aws/en/genie/knowledge-store#view-columns).
* **Prompt matching**: Format assistance and entity matching help Genie match user language to actual data values, correct misspellings, and generate more accurate SQL. See  [Prompt matching overview](/aws/en/genie/knowledge-store#prompt-matching-overview).
* **Join relationships**: Define relationships between tables so Genie can construct accurate `JOIN` statements. See  [Define join relationships](/aws/en/genie/knowledge-store#join-overview).
* **SQL expressions**: Define reusable measures, filters, and dimensions that capture business logic, such as KPIs and common filtering conditions. See [Define SQL expressions](/aws/en/genie/knowledge-store#sql-expressions).

## Add SQL examples and instructions[â](#-add-sql-examples-and-instructions "Direct link to -add-sql-examples-and-instructions")

You can add sample SQL queries, Unity Catalog functions, and plain-text instructions to help generate accurate responses. Click **Configure** > **Instructions**. Use the **SQL Queries** tab to manage queries and Unity Catalog functions. Use the **Text** tab to add plain text instructions.

You can add up to 100 instructions in total for a Genie space. Instruction types contribute to the count in the following ways:

* Each example SQL query counts as one.
* Each SQL function counts as one.
* The entire **General instructions** text block counts as one.

SQL expressions have a separate limit of 200 and do not count toward the instruction limit. See [Define SQL expressions](/aws/en/genie/knowledge-store#sql-expressions).

A Genie space aims to provide consistent and predictable responses based on clear and precise guidance. Because Genie operates in a nondeterministic manner, itâs important to make the guidance free from conflicting or ambiguous information to minimize the risk of undesirable responses. When setting up the space, a key task is to review and resolve any inconsistencies. This helps to achieve reliable results.

### Add example SQL queries and functions[â](#-add-example-sql-queries-and-functions "Direct link to -add-example-sql-queries-and-functions")

Use the **SQL Queries** tab to add the following:

* **Example queries (Recommended):** Example SQL queries help Genie generate the correct SQL to answer common user questions. Queries can be static or parameterized. For each example SQL query, provide the SQL and use the most typical phrasing of the userâs question as the title. This improves Genieâs ability to match prompts to the example. Genie can either use the example query directly or learn from it to handle similar questions. When a parameterized query is used, the response is marked as **Trusted**. Users with CAN EDIT privileges in the space can view the query used to generate the response, which helps with troubleshooting and refinement.
* **SQL functions:** For questions that cannot be answered with a static or parameterized SQL query, you can register a custom function to Unity Catalog. Functions can be shared across your teams and used by Genie to answer specific questions. Responses that are answered using a SQL function are marked as **Trusted**. To learn more about using SQL functions in your Genie space, see [Use trusted assets in Genie spaces](/aws/en/genie/trusted-assets).

### How Genie uses example queries[â](#how-genie-uses-example-queries "Direct link to How Genie uses example queries")

Example queries show Genie how to use the available data to answer questions. Enter a sample question into the text field, and then enter a SQL query that answers that question. Write the sample question the way a user would naturally ask it. When Genie receives a matching question, it can use the example query directly to provide an answer. When Genie gets a similar question, it uses clues from the example query to learn and structure the SQL provided in the response. Focus on providing samples that highlight logic that is unique to your organization and data, as in the following example:

SQL

```
  -- Return our current total open pipeline by region.
  -- Opportunities are only considered pipelines if they are tagged as such.
  SELECT
    a.region__c AS `Region`,
    sum(o.amount) AS `Open Pipeline`
  FROM
    sales.crm.opportunity o
    JOIN sales.crm.accounts a ON o.accountid = a.id
  WHERE
    o.forecastcategory = 'Pipeline' AND
    o.stagename NOT ILIKE '%closed%'
  GROUP BY ALL;
```

#### Add query parameters[â](#add-query-parameters "Direct link to Add query parameters")

Parameterized example queries allow space users to specify a specific value to be inserted in the query at runtime. To learn more about working with parameterized queries, see [Use parameters in SQL queries](/aws/en/genie/query-params).

#### Provide usage guidance[â](#provide-usage-guidance "Direct link to Provide usage guidance")

You can provide Genie additional context to explain when an example query is particularly relevant.

To add usage guidance:

1. Click **Configure** > **Instructions** > **SQL Queries** to access the list of example queries.
2. Click an example query.
3. Click **Usage guidance** near the bottom of the screen.
4. Enter details about how and when to use this example query.

### How does Genie use SQL functions?[â](#how-does-genie-use-sql-functions "Direct link to How does Genie use SQL functions?")

SQL functions are useful when a question involves complex logic that cannot be captured with a static or parameterized query. They are stored in Unity Catalog and can be called by Genie using user-supplied parameters. Genie cannot view or modify the SQL used in the function, making this approach well-suited for logic that should not be surfaced or changed. For guidance on registering a function in Unity Catalog, see [Create a SQL table function](/aws/en/sql/language-manual/sql-ref-syntax-ddl-create-sql-function#create-a-sql-table-function) and [User-defined functions (UDFs) in Unity Catalog](/aws/en/udf/unity-catalog).

### Provide instructions[â](#-provide-instructions "Direct link to -provide-instructions")

Click the **Text** tab to write plain text instructions that help Genie understand how to respond to specific questions about your business. You can format the instructions as a single comprehensive note or categorize them by topic for better organization.

Instructions help guide Genie's responses so that it can process the unique jargon, logic, and concepts in a given domain. General text instructions apply to all prompts. If an instruction is relevant only to a subset of prompts, it should be included as an example query or function, or documented in the relevant table as comments or metadata. Text instructions are *only* for context that should be applied globally and do not fit into the other formats.

The following example includes information you could i


================================================================================

## 4. Build a knowledge store for more reliable Genie spaces

**URL:** https://docs.databricks.com/aws/en/genie/knowledge-store
**Crawl depth:** 0

---

* * [Business intelligence](/aws/en/ai-bi/)* [Genie spaces](/aws/en/genie/)* For space authors* Build a knowledge store

On this page

Last updated on **Mar 4, 2026**

# Build a knowledge store for more reliable Genie spaces

The Genie knowledge store allows you to curate and enhance your space through localized metadata, prompt matching, and structured SQL instructions. These features help Genie understand your data and generate more accurate and relevant responses.

## What is a knowledge store?[â](#what-is-a-knowledge-store "Direct link to What is a knowledge store?")

A knowledge store is a collection of curated semantic definitions that enhances Genie's understanding of your data and improves response accuracy.

The knowledge store consists of:

* **Space-level metadata customization**: Space-specific descriptions for tables, columns, and business terms and synonyms.
* **Space-level data customization**: Simplified, focused datasets without changing the underlying Unity Catalog tables.
* **Prompt matching**: Examples that help Genie match values that are most relevant to the user's question and correct spelling issues in user prompts. This includes [format assistance](#manage-format-assistance) and [entity matching](#configure-entity-matching).
* **Join relationships**: Defined table relationships for accurate `JOIN` statements.
* **SQL expressions**: Structured definitions of measures, filters, and dimensions that capture business logic.

All knowledge store configurations are scoped to your Genie space and do not affect Unity Catalog metadata or other Databricks assets.

## Manage knowledge store metadata[â](#manage-knowledge-store-metadata "Direct link to Manage knowledge store metadata")

Teach Genie about the data in your space by providing local table and column descriptions and adding column synonyms that align with common business terms. Simplify datasets by hiding unnecessary or duplicate columns to keep Genie focused.

These practices improve usability for users who do not have direct permissions on the underlying tables, and they also support quicker iterations when updating instruction versions.

To access space-level metadata, click **Configure > Data** in your Genie space. Then click a table name to view its metadata and columns.

### View columns[â](#-view-columns "Direct link to -view-columns")

Click a table name to see an overview of the column names and details. The following example shows a sample from a table named `accounts`.

* **Description:** Genie uses metadata to understand your data and generate accurate responses. The default table description shows the Unity Catalog metadata associated with your data asset. Edit this description to add specific directions that help Genie author SQL for your space. Click **Reset** to restore the Unity Catalog description.
* **Columns:** Column names and descriptions are included in the column list. Each column is labeled with tags that show whether it includes **Format assistance** or **Entity matching**. See  [Prompt matching overview](#prompt-matching-overview).

### Hide or show relevant columns[â](#hide-or-show-relevant-columns "Direct link to hide-or-show-relevant-columns")

Columns can be managed individually or in bulk. Use the following instructions to hide or show columns.

* **Hide a single column**: Click the  next to the column name.
* **Hide multiple columns**:
  + Select the checkboxes for the columns you want to hide.
  + From the **Actions** menu, select **Hide selected columns**.
* **Undo changes**: Repeat the same steps to show a column that was hidden.

### Edit column metadata[â](#edit-column-metadata "Direct link to Edit column metadata")

You can customize the following for each column:

* **Description**: Space-specific column descriptions that enhance Genie's understanding.
* **Synonyms**: Business terms and keywords that help match user language to column names.
* **Advanced settings**: Prompt matching controls.
  + **Format assistance**: Turn sampling of representative values on or off.
  + **Entity matching**: Enable or disable entity matching for categorical columns.

To edit column metadata:

1. Click the  pencil icon next to a column name.
2. Edit the description and synonyms for the column.
3. If necessary, click **Advanced settings** to open prompt matching controls.
4. Click **Save** to keep your changes and close the dialog.

## Prompt matching overview[â](#-prompt-matching-overview "Direct link to -prompt-matching-overview")

Prompt matching allows Genie to match columns and values that are most relevant to the user's question, and correct spelling issues in user prompts. This improves Genie's accuracy and helps generate more reliable SQL queries.

When a user asks a question in Genie, the phrasing is often conversational and can include errors such as misspellings. In these cases, the values in the prompt might not match the structure or values in the data. This can cause Genie to misinterpret the question and generate incorrect SQL.

### Example[â](#example "Direct link to Example")

Review the following example:

> "Show me car sales in Florida for Q1."

If the data uses state abbreviations (such as `FL`), and Genie cannot access the values for that column, Genie might generate SQL that includes `ILIKE '%Florida%'`, which returns no results.

Enabling entity matching on the `state` column allows Genie to access representative values. With this context, Genie can recognize that `FL` corresponds to "Florida" and generate more accurate SQL.

|  |  |  |  |
| --- | --- | --- | --- |
| Without entity matching With entity matching|  |  | | --- | --- | | `WHERE state ILIKE '%Florida%'` `WHERE state = 'FL'` | | | |

### Prompt matching components[â](#-prompt-matching-components "Direct link to -prompt-matching-components")

* **Format assistance**: Format assistance provides representative values for all eligible columns, helping Genie understand data types and formatting patterns. Representative values for prompt matching are generated using the author's data permissions. These values become part of the space's shared context and help Genie interpret user prompts more accurately for all space participants.
* **Entity matching**: Entity matching provides curated lists of distinct values for up to 120 columns where users are likely to reference specific entries, such as states and product categories. This helps Genie match user terminology to actual data values. Each column can include up to 1,024 distinct values, each up to 127 characters in length. Entity matching data is stored in your workspace's storage bucket.

Genie automatically provides format assistance and entity matching for eligible columns as you add tables to the space. Tables with row filters or column masks are excluded from prompt matching.

## Manage prompt matching[â](#manage-prompt-matching "Direct link to Manage prompt matching")

Control which columns provide format assistance and entity matching to optimize Genie's understanding of your data. Prompt matching is enabled by default for all Genie spaces.

### Manage format assistance[â](#manage-format-assistance "Direct link to manage-format-assistance")

Format assistance is automatically applied when you add tables to a Genie space.

To turn off format assistance for a column:

1. Click **Configure > Data** in your Genie space.
2. Click a table name to view its columns.
3. Click the  pencil icon next to the column name.
4. Click **Advanced**.
5. Turn **Format assistance** off.

This action also automatically disables entity matching for that column. If necessary, use this setting to turn **Format assistance** back on.

### Configure entity matching[â](#configure-entity-matching "Direct link to configure-entity-matching")

Genie generates responses using your prompt, relevant table metadata, prompt matching capabilities, error signals, and any input code or queries. When a column has entity matching enabled, Genie leverages the stored values to match user prompts to actual data more accurately. This produces more reliable SQL queries. Entity matching significantly improves Genie's accuracy, especially when combined with clear example queries and well-crafted instructions. See [Curate an effective Genie space](/aws/en/genie/best-practices) for more guidance.

Genie prevents you from enabling entity matching on tables with [row filters or column masks](/aws/en/data-governance/unity-catalog/filters-and-masks/). However, space authors must disable entity matching for views that reference tables with row filters or column masks, or for [dynamic views](/aws/en/views/dynamic).

Entity matching only supports string columns. The following list includes examples of the types of data that work well with entity matching:

* State or country codes
* Product categories
* Status codes
* Department names

To enable entity matching, **Format assistance** must be turned on. Then, use the following steps:

1. Click **Configure > Data** in your Genie space.
2. Click a table name to view its columns.
3. Click the  pencil icon next to the column name.
4. Click **Advanced**.
5. Turn **Entity matching** on.
6. To disable entity matching for a column, turn **Entity matching** off.

### Refresh or remove prompt matching data[â](#refresh-or-remove-prompt-matching-data "Direct link to refresh-or-remove-prompt-matching-data")

Refreshing prompt matching data updates a column's stored values. Refresh values if:

* New values have been added to the column.
* The format of existing values has changed.

To refresh prompt matching data, click  the kebab menu in the column view, then **Refresh prompt matching**.

## Define join relationships[â](#-define-join-relationships "Direct link to -define-join-relationships")

Help Genie create accurate `JOIN` statements by defining table relationships:

1. Click **Joins**.
2. Click **Add**.
3. Select left and right tables from the drop-down menus.
4. Enter a **Join condition** (for example, `accounts.id = opportunity.accountid`)
   * For more complicated join conditions, click **Use SQL expression** and then record the join condition as a SQL expression.
5. Select a **Relationship Type**:
   * **Many to one**: Multiple left rows map to one right row
   * **One to many**: One left row maps to multiple right rows
   * **One to one**: One left row maps to at most one right row

note

When multiple joins exist between the same tables or self-joins are used, Genie automatically generates aliases for the right-hand table to avoid ambiguity.

## Define SQL expressions[â](#define-sql-expressions "Direct link to define-sql-expressions")

SQL expressions provide a structured, guided way to teach Genie about common business terms such as KPIs, attributes, and conditions. Genie then uses these definitions when a user asks about these business terms.

SQL expressions complement [example SQL queries](/aws/en/genie/set-up#example-queries), specified in instructions. SQL expressions define reusable business concepts, but example SQL queries are more helpful for teaching Genie how to approach common user prompt formats. For example, if users commonly ask for "a breakdown of performance", an example SQL query can show that this means closed sales by region, sales rep, and manager.

SQL expressions work best when you need to:

* Provide structured definitions for KPIs and metrics, such as profit margin or conversion rate
* Give Genie explicit context about how to calculate important values
* Define additional dimensions for the dataset, such as month or customer segment
* Teach Genie filters for business conditions, such as large orders or orders before a specific time

### SQL expression types[â](#sql-expression-types "Direct link to SQL expression types")

You can define the following types of SQL expressions:

* **Measures**: Key performance indicators (KPIs) and metrics. Define the name, SQL calculation, and synonyms.
* **Filters**: Common filtering conditions. Define the name, SQL filter logic, and synonyms.
* **Dimensions**: Attributes for grouping and analyzing data. Define the name, SQL expression, and synonyms.

Use the following instructions to define SQL expressions:

1. Click **Configure** > **Instructions** > **SQL Expressions**
2. Click **Add**. Choose **Filter**, **Measure**, or **Dimension**.
3. In the **Name** field, enter a name for the expression.
4. In the **Code** field, enter the SQL expression.

* Filter expressions should evaluate to a boolean condition.
* Measure expressions should calculate an aggregation over multiple rows in the table.
* Dimension expressions should alter the value of each row from the existing data.

1. In the **Synonyms** field, enter common ways that users might refer to the expressions colloquially.
2. In the **Instructions** field, enter specific instructions that tell Genie what the expression is for and how to work with it.

## Knowledge mining recommendations[â](#knowledge-mining-recommendations "Direct link to knowledge-mining-recommendations")

Knowledge mining helps improve Genie by automatically suggesting updates to the knowledge store, reducing manual curation and improving answer accuracy.

First, Genie analyzes Unity Catalog metadata for the tables and views connected to your space. Primary and foreign keys defined in your schema are automatically saved as join relationships in the Genie space.

Genie also learns from author interactions in conversations. When an author thumbs-up a response or downloads query results, Genie analyzes the query and identifies useful logic that can improve accuracy on future questions. It might suggest new SQL expressions (measures, filters, or dimensions) as well as additional join relationships to add to the knowledge store.

## Next steps[â](#next-steps "Direct link to Next steps")

Use the following links to help you continue to build your Genie space.

* Add context to your Genie space to help generate accurate responses. See  [Add SQL examples and instructions](/aws/en/genie/set-up#add-context)
* Learn best practices for optimizing your Genie space. See [Curate an effective Genie space](/aws/en/genie/best-practices)
* Evaluate and improve your space's performance. See [Use benchmarks in a Genie space](/aws/en/genie/benchmarks)

* [What is a knowledge store?](#what-is-a-knowledge-store)* [Manage knowledge store metadata](#manage-knowledge-store-metadata)
    + [View columns](#-view-columns)+ [Hide or show relevant columns](#hide-or-show-relevant-columns)+ [Edit column metadata](#edit-column-metadata)* [Prompt matching overview](#-prompt-matching-overview)
      + [Example](#example)+ [Prompt matching components](#-prompt-matching-components)* [Manage prompt matching](#manage-prompt-matching)
        + [Manage format assistance](#manage-format-assistance)+ [Configure entity matching](#configure-entity-matching)+ [Refresh or remove prompt matching data](#refresh-or-remove-prompt-m


================================================================================

## 5. Use parameters in SQL queries

**URL:** https://docs.databricks.com/aws/en/genie/query-params
**Crawl depth:** 0

---

* * [Business intelligence](/aws/en/ai-bi/)* [Genie spaces](/aws/en/genie/)* For space authors* Use parameters

On this page

Last updated on **Mar 18, 2025**

# Use parameters in SQL queries

This article explains how to use parameters when writing example SQL instructions in a Genie space.

## Why use parameters?[â](#why-use-parameters "Direct link to Why use parameters?")

Parameters let you write example queries with placeholders for specific values to be substituted at runtime. With parameters, Genie can take specific inputs from user questions and reuse the structure of an example query to provide verified answers as trusted assets. For example, you could adjust the previous SQL query to include a parameter that filters by the `o.forecastcategory` value, enabling the query to address questions about opportunities tagged in different forecast categories. For more information about how to use parameterized queries to generate responses labeled as trusted assets, see [Use trusted assets in Genie spaces](/aws/en/genie/trusted-assets).

The following example query calculates the total open pipeline value sales opportunities by region. It includes a parameter for the `o.forecastcategory` value. Parameters use the same syntax as named parameter markers. For more guidance on using parameters in a Genie space, see [Work with query parameters](/aws/en/sql/user/queries/query-parameters) and [Named parameter markers](/aws/en/sql/language-manual/sql-ref-parameter-marker#named-parameter-markers).

SQL

```
-- Return our current pipeline at a stage by region.
-- Opportunities are only considered pipelines if they are tagged as such.
  SELECT
    a.region__c AS `Region`,
    sum(o.amount) AS `Open Pipeline`
  FROM
    sales.crm.opportunity o
    JOIN sales.crm.accounts a ON o.accountid = a.id
  WHERE
    o.forecastcategory = :forecast_category AND
    o.stagename NOT ILIKE '%closed%'
  GROUP BY ALL;
```

To add a parameter to a query:

1. Place your cursor where you want to place the parameter in your query.
2. Click **Add parameter** to insert a new parameter.

   This creates a new parameter with the default name `parameter`. To change the default name, replace it in the query editor. You can also add parameters by typing a colon followed by a parameter name (`:parameter_name`) into the editor.

## Edit a query parameter[â](#edit-a-query-parameter "Direct link to Edit a query parameter")

To edit a parameter, do the following:

1. Click  next to the parameter name. A **Parameter details** dialog appears and includes the following configuration options:

   * **Keyword**: The keyword that represents the parameter in the query. The keyword can only be changed by directly updating the text in the query.
   * **Display name**: The human-readable name that Genie uses in the chat experience. When Genie generates a response using a parameterized query, it includes the display name and associated value in the response.
   * **Type**: Supported types include **String**, **Date**, **Date and Time**, and **Numeric**.

     + The default type is **String**.
     + The **Numeric** datatype allows you to specify between **Decimal** and **Integer**. The default numeric type is **Decimal**.

     note

     If the actual input value does not match the selected parameter type, Genie treats the input value as the incorrect type, which can lead to inaccurate results.
2. Click another part of the UI to close the dialog.

## Parameterized query responses[â](#parameterized-query-responses "Direct link to Parameterized query responses")

When the exact text of a parameter is used in a response, the response is marked trusted. This means that Genie identified, based on the space's context, the user question matched the intent of an example question or query.

The **Trusted** label lets space users know that Genie's response is based on a vetted SQL query. They can see the generated SQL and paramter values that are used in the response.

* [Why use parameters?](#why-use-parameters)* [Edit a query parameter](#edit-a-query-parameter)* [Parameterized query responses](#parameterized-query-responses)


================================================================================

## 6. Use trusted assets in Genie spaces

**URL:** https://docs.databricks.com/aws/en/genie/trusted-assets
**Crawl depth:** 0

---

* * [Business intelligence](/aws/en/ai-bi/)* [Genie spaces](/aws/en/genie/)* For space authors* Trusted assets

On this page

Last updated on **Mar 6, 2026**

# Use trusted assets in Genie spaces

This page defines trusted assets and explains how to use them to provide verified answers in a Genie space.

## What are trusted assets?[â](#what-are-trusted-assets "Direct link to What are trusted assets?")

Trusted assets are predefined functions and example queries meant to provide verified answers to questions that you anticipate from users. When a user submits a question that invokes a trusted asset, it's indicated in the response, adding an extra layer of assurance to the accuracy of the results.

Trusted assets can include the following:

* **Parameterized example SQL queries**: When a parameterized example SQL query is used to generate a response, the reponse is labeled a trusted asset. The response includes the values used as arguments in the query. Users can edit the parameter value in the response.
* **User-defined table functions (UDFs)**: You can define custom functions and register them with Unity Catalog. Then, you can add those functions as trusted assets when you're setting up instructions in your Genie space. See [Create a SQL table function](/aws/en/sql/language-manual/sql-ref-syntax-ddl-create-sql-function#create-a-sql-table-function) and [User-defined functions (UDFs) in Unity Catalog](/aws/en/udf/unity-catalog).

note

Trusted assets are not a substitute for other instructions. Databricks recommends using trusted assets for well-established recurring questions. They provide exact answers to specific questions.

## Why create trusted assets?[â](#why-create-trusted-assets "Direct link to Why create trusted assets?")

When using any AI tool, users should evaluate the accuracy of generated responses. Typically, they do this by considering whether the answer makes sense and effectively addresses their question. With Genie, a response is delivered as a table of results. Users can review the generated SQL that creates the result set, but non-technical users might not have the background to interpret the SQL statement or assess the correctness of the answer. Trusted assets help reduce the likelihood of these users encountering responses that are misleading, incorrect, or difficult to interpret.

When a user receives a response that is labeled as **Trusted**, it means that a domain expert has added the SQL statement used to generate the results as an instruction in the space.

## What's the difference between trusted assets and example SQL queries?[â](#whats-the-difference-between-trusted-assets-and-example-sql-queries "Direct link to What's the difference between trusted assets and example SQL queries?")

Trusted assets provide verified answers to questions you expect Genie space users to ask. When a trusted asset can answer a user's question, the instruction you have stored as a trusted asset runs and returns the specified result set. **Example SQL Queries** that include parameters and **SQL Functions** that you add to a space's context are treated as trusted assets.

* **Example SQL Queries (with parameters)**: When a parameterized example query's exact text is used to generate a response, the response is automatically labeled as **Trusted**. Space users can edit the parameter value in a response and rerun the query using the new value.
* **SQL Functions**: You can write custom SQL functions tailored to handle your data and address company-specific questions. Genie does not consider the SQL content of your trusted assets when responding to questions.

note

If the exact text of the query is not used, or the example query does not use parameters, the example queries provide context and guide Genie in generating the SQL statements, but are not marked as **Trusted**.

## Define a trusted asset[â](#define-a-trusted-asset "Direct link to Define a trusted asset")

Defining a trusted asset starts with identifying a likely question. For example, suppose you're working with a sales pipeline dataset, and a common question that a sales manager might ask is, âWhat are the open sales opportunities in my region?â

### Example: Create a UDF to answer the question[â](#example-create-a-udf-to-answer-the-question "Direct link to Example: Create a UDF to answer the question")

The following steps outline how to write a test query and use it to create a UDF:

1. Use the [SQL editor](/aws/en/sql/user/sql-editor/) or a [notebook](/aws/en/notebooks/basic-editing) to define and test a SQL query that answers the question.

This query joins two tables and returns a dataset of open opportunities listed in the `âPipelineâ` forecast category. In this step, the goal is to write a basic query that returns the expected results.

SQL

```
SELECT
  o.id AS `OppId`,
  a.region__c AS `Region`,
  o.name AS `Opportunity Name`,
  o.forecastcategory AS `Forecast Category`,
  o.stagename,
  o.closedate AS `Close Date`,
  o.amount AS `Opp Amount`
FROM
users.user_name.opportunity o
JOIN catalog.schema.accounts a ON o.accountid = a.id
WHERE
o.forecastcategory = 'Pipeline'
AND o.stagename NOT LIKE '%closed%';
```

1. Define a Unity Catalog function.

Your Unity Catalog function should parameterize the query and produce results matching the specific conditions you expect the user to ask about. For example, suppose the sales manager wants to narrow the result set by focusing on a particular region or group of regions.

The following example defines a Unity Catalog function that takes a list of regions as a parameter and returns a table. The function return is almost identical to the SQL statement in the previous step, except the `WHERE` clause has been modified to filter the results by region if a region has been provided. The comments provided in the function definitions are critical for instructing the Genie space on when and how to invoke this function.

* **Parameter comments**: The `open_opps_in_region` function expects an array of strings as a parameter. The comment includes an example of the expected input. If no parameter is supplied, the default value is `NULL`. See [Tips for writing functions](#tips) for more on including optional parameters and comments.
* **Function comments**: The comment in the SQL table function provides a detailed explanation of what the function does. This is critical because it informs Genie when to use the function as a response to user questions. The comment should describe the function's purpose as precisely as possible. This information guides Genie in recognizing the function's relevance to specific questions.

SQL

```
CREATE
OR REPLACE FUNCTION users.user_name.open_opps_in_region (
  regions ARRAY < STRING >
  COMMENT 'List of regions.  Example: ["APAC", "EMEA"]' DEFAULT NULL
) RETURNS TABLE
COMMENT 'Addresses questions about the pipeline in the specified regions by returning
a list of all the open opportunities. If no region is specified, returns all open opportunities.
Example questions: "What is the pipeline for APAC and EMEA?", "Open opportunities in
APAC"'
RETURN
  SELECT
  o.id AS `OppId`,
  a.region__c AS `Region`,
  o.name AS `Opportunity Name`,
  o.forecastcategory AS `Forecast Category`,
  o.stagename,
  o.closedate AS `Close Date`,
  o.amount AS `Opp Amount`
  FROM
  catalog.schema.opportunity o
  JOIN catalog.schema.accounts a ON o.accountid = a.id
  WHERE
  o.forecastcategory = 'Pipeline'
  AND o.stagename NOT LIKE '%closed%'
  AND (
    isnull(open_opps_in_region.regions)
    OR array_contains(open_opps_in_region.regions, region__c)
  );
```

When you run the code to create a function, it's registered to the currently active schema by default. See [User-defined functions (UDFs) in Unity Catalog](/aws/en/udf/unity-catalog). See [Create a SQL table function](/aws/en/sql/language-manual/sql-ref-syntax-ddl-create-sql-function#create-a-sql-table-function) for syntax and examples.

1. Add a trusted asset.

   After the function is created in Unity Catalog, a user with at least CAN EDIT permission on the Genie space can add it to the Genie space. Click **Configure** > **Context** > **SQL Queries**. Then, click **Add**.

## Required permissions[â](#required-permissions "Direct link to Required permissions")

Users with at least CAN EDIT permission on a Genie space can add or remove trusted assets.

Genie space users must have `CAN USE` permission on the catalog and schema that contains the function. To invoke a trusted asset, they must have `EXECUTE` permission on the function in Unity Catalog. Unity Catalog securable objects inherit permissions from their parent containers. See [Securable objects in Unity Catalog](/aws/en/data-governance/unity-catalog/manage-privileges/privileges#securable-objects).

To simplify sharing in a Genie space, Databricks recommends creating a dedicated schema to contain all the functions you want to use in your Genie space.

## Tips for writing functions[â](#tips-for-writing-functions "Direct link to tips-for-writing-functions")

Review the following examples to learn how to create dynamic functions for trusted assets.

### Include a default parameter value[â](#include-a-default-parameter-value "Direct link to Include a default parameter value")

You can specify a default value for a parameter. Use the `DEFAULT` clause in the function signature as shown in the following example:

SQL

```
countries ARRAY<STRING> COMMENT 'List of countries' DEFAULT ARRAY()
```

### Include example parameter values[â](#include-example-parameter-values "Direct link to Include example parameter values")

For columns with a set enumeration of values, increase accuracy by defining them clearly in the comment. The following example provides a sample list of values:

SQL

```
regions ARRAY < STRING > COMMENT 'List of regions. Values: ["AF","AN","AS", "EU", "NA", "OC", "SA", NULL]'
```

### Create an optional parameter[â](#create-an-optional-parameter "Direct link to Create an optional parameter")

To create an optional parameter, set the default parameter to `NULL` as shown in the following example:

SQL

```
min_date STRING DEFAULT NULL
```

### Specify formatting with comments[â](#specify-formatting-with-comments "Direct link to Specify formatting with comments")

You can specify an exact format for a parameter by including it in a comment, as shown in the following example:

SQL

```
min_date STRING COMMENT 'minimum date (included) for a transaction, in `yyyy-mm-dd` format'
```

### Explictly check for `NULL` values[â](#explictly-check-for-null-values "Direct link to explictly-check-for-null-values")

If you include an optional parameter, one possible value you should expect is `NULL`. Because comparison with `NULL` can yield unpredictable results, you should explicitly build a check for `NULL` values into your function. The following example provides example syntax:

SQL

```
WHERE (isnull(min_date) OR created_date >= min_date)
```

* [What are trusted assets?](#what-are-trusted-assets)* [Why create trusted assets?](#why-create-trusted-assets)* [What's the difference between trusted assets and example SQL queries?](#whats-the-difference-between-trusted-assets-and-example-sql-queries)* [Define a trusted asset](#define-a-trusted-asset)
        + [Example: Create a UDF to answer the question](#example-create-a-udf-to-answer-the-question)* [Required permissions](#required-permissions)* [Tips for writing functions](#tips-for-writing-functions)
            + [Include a default parameter value](#include-a-default-parameter-value)+ [Include example parameter values](#include-example-parameter-values)+ [Create an optional parameter](#create-an-optional-parameter)+ [Specify formatting with comments](#specify-formatting-with-comments)+ [Explictly check for `NULL` values](#explictly-check-for-null-values)


================================================================================

## 7. Use benchmarks in a Genie space

**URL:** https://docs.databricks.com/aws/en/genie/benchmarks
**Crawl depth:** 0

---

* * [Business intelligence](/aws/en/ai-bi/)* [Genie spaces](/aws/en/genie/)* For space authors* Benchmarks

On this page

Last updated on **Oct 9, 2025**

# Use benchmarks in a Genie space

This page explains how to use benchmarks to evaluate the accuracy of your Genie space.

## Overview[â](#overview "Direct link to Overview")

Benchmarks allow you to create a set of test questions that you can run to assess Genie's overall response accuracy. A well-designed set of benchmarks covering the most frequently asked user questions helps evaluate the accuracy of your Genie space as you refine it. Each Genie space can contain up to 500 benchmark questions.

Benchmark questions run as new conversations. They do not carry the same context as a threaded Genie conversation. Each question is processed as a new query, using the instructions defined in the space, including any provided example SQL and SQL functions.

## Add benchmark questions[â](#add-benchmark-questions "Direct link to add-benchmark-questions")

Benchmark questions should reflect different ways of phrasing the common questions your users ask. You can use them to check Genie's response to variations in question phrasing or different question formats.

When creating a benchmark question, you can optionally include a SQL query whose result set is the correct answer. During benchmark runs, accuracy is assessed by comparing the result set from your SQL query to the one generated by Genie. You can also use Unity Catalog SQL functions as gold standard answers for benchmarks.

To add a benchmark question:

1. Near the top of the Genie space, click **Benchmarks**.
2. Click **Add benchmark**.
3. In the **Question** field, enter a benchmark question to test.
4. (Optional) Provide a SQL query that answers the question. You can write your own query by typing in the **SQL Answer** text field, including Unity Catalog SQL functions. Alternatively, click **Generate SQL** to have Genie write the SQL query for you. Use a SQL statement that accurately answers the question you entered.

   note

   This step is recommended. Only questions that include this example SQL statement can be automatically assessed for accuracy. Any questions that do not include a **SQL Answer** require manual review to be scored. If you use the **Generate SQL** button, review the statement to be sure that it's accurately answering the question.
5. (Optional) Click **Run** to run your query and view the results.
6. When you're finished editing, click **Add benchmark**.
7. To update a question after saving, click the  pencil icon to open the **Update question** dialog.

### Use benchmarks to test alternate question phrasings[â](#use-benchmarks-to-test-alternate-question-phrasings "Direct link to Use benchmarks to test alternate question phrasings")

When evaluating the accuracy of your Genie space, it's important to structure tests to reflect realistic scenarios. Users may ask the same question in different ways. Databricks recommends adding multiple phrasings of the same question and using the same example SQL in your benchmark tests to fully assess accuracy. Most Genie spaces should include between two and four phrasings of the same question.

## Run benchmark questions[â](#run-benchmark-questions "Direct link to Run benchmark questions")

Users with at least CAN EDIT permissions in a Genie space can run a benchmark evaluation at any time. You can run all benchmark questions or select a subset of questions to test.

For each question, Genie interprets the input, generates SQL, and returns results. The generated SQL and results are then compared against the **SQL Answer** defined in the benchmark question.

To run all benchmark questions:

1. Near the top of the Genie space, click **Benchmarks**.
2. Click **Run benchmarks** to start the test run.

To run a subset of benchmark questions:

1. Near the top of the Genie space, click **Benchmarks**.
2. Select the checkboxes next to the questions you want to test.
3. Click **Run selected** to start the test run on the selected questions.

You can also select a subset of questions from a previous benchmark result and rerun those specific questions to test improvements.

Benchmarks continue to run when you navigate away from the page. You can check the results on the **Evaluation** tab when the run is complete.

## Interpret ratings[â](#interpret-ratings "Direct link to interpret-ratings")

The following criteria determine how Genie responses are rated:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Condition Rating|  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Genie generates SQL that exactly matches the provided **SQL Answer** **Good**|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Genie generates a result set that exactly matches the result set produced by the **SQL Answer** **Good**|  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Genie generates a result set with the same data as the **SQL Answer** but sorted differently **Good**|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | Genie generates a result set with numeric values that round to the same 4 significant digits as the **SQL Answer** **Good**|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | Genie generates SQL that produces an empty result set or returns an error **Bad**|  |  |  |  | | --- | --- | --- | --- | | Genie generates a result set that includes extra columns compared to the result set produced by the **SQL Answer** **Bad**|  |  | | --- | --- | | Genie generates a single cell result that's different from the single cell result produced by the **SQL Answer** **Bad** | | | | | | | | | | | | | | | |

**Manual review needed**: Responses are marked with this label when Genie cannot assess correctness or when Genie-generated query results do not contain an exact match with the results from the provided **SQL Answer**. Any benchmark questions that do not include a **SQL Answer** must be reviewed manually.

## Access benchmark evaluations[â](#access-benchmark-evaluations "Direct link to Access benchmark evaluations")

You can access all of your benchmark evaluations to track accuracy in your Genie space over time. When you open a space's **Benchmarks**, a timestamped list of evaluation runs appears in the **Evaluations** tab. If no evaluation runs are found, see [Add benchmark questions](#add-benchmark-questions) or [Run benchmark questions](#run-benchmark-questions).

The **Evaluations** tab shows an overview of evaluations and their performance reported in the following categories:

**Evaluation name**: A timestamp that indicates when an evaluation run occurred. Click the timestamp to see details for that evaluation.
**Execution status**: Indicates if the evaluation is completed, paused, or unsuccessful. If an evaluation run includes benchmark questions that do not have predefined SQL answers, it is marked for review in this column.
**Accuracy**: A numeric assessment of accuracy across all benchmark questions. For evaluation runs that require manual review, an accuracy measure appears only after those questions have been reviewed.
**Created by**: Indicates the name of the user who ran the evaluation.

## Review individual evaluations[â](#review-individual-evaluations "Direct link to review-individual-evaluations")

You can review individual evaluations to get a detailed look at each response. You can edit the assessment for any question and update any items that need manual review.

To review individual evaluations:

1. Near the top of the Genie space, click **Benchmarks**.
2. Click the timestamp for any evaluation in the **Evaluation name** column to open a detailed view of that test run.
3. Use the question list on the left side of the screen to see a detailed view of each question.
4. Review and compare the **Model output** response with the **Ground truth** response.

   For results rated as incorrect, an explanation appears describing why the result was rated as **Bad**. This helps you understand specific differences between the generated output and the expected ground truth.

   note

   The results of these responses appear in the evaluation details for one week. After one week, the results are no longer visible. The generated SQL statement and the example SQL statement remain.
5. Click **Update ground truth** to save the response as the new **Ground truth** for this question. This is useful if no ground truth exists, or if the response is better or more accurate than the existing ground truth statement.
6. Click the  on the label to edit the assessment.

   Mark each result as **Good** or **Bad** to get an accurate score for this evaluation.

* [Overview](#overview)* [Add benchmark questions](#add-benchmark-questions)
    + [Use benchmarks to test alternate question phrasings](#use-benchmarks-to-test-alternate-question-phrasings)* [Run benchmark questions](#run-benchmark-questions)* [Interpret ratings](#interpret-ratings)* [Access benchmark evaluations](#access-benchmark-evaluations)* [Review individual evaluations](#review-individual-evaluations)


================================================================================

## 8. Curate an effective Genie space

**URL:** https://docs.databricks.com/aws/en/genie/best-practices
**Crawl depth:** 0

---

* * [Business intelligence](/aws/en/ai-bi/)* [Genie spaces](/aws/en/genie/)* For space authors* Best practices

On this page

Last updated on **Feb 17, 2026**

# Curate an effective Genie space

The goal of curating a Genie space is to create an environment where business users can pose natural language questions and receive accurate, consistent answers based on their data. Genie spaces use advanced models that generate sophisticated queries and understand general world knowledge.

Most business questions are domain-specific, so a space curator's role is to bridge the gap between that general world knowledge and the specialized language used in a specific domain or by a particular company. Curators use metadata and instructions to help Genie accurately interpret and respond to business users' questions. This page outlines best practices and principles to guide you in developing a successful space.

## Best practices for defining a new space[â](#best-practices-for-defining-a-new-space "Direct link to Best practices for defining a new space")

Think of Genie as a new data analyst joining your company. Like any new team member, Genie needs clear context to be effective. It relies on quality table and column descriptions to understand what the data represents, example SQL queries to learn how to solve common problems, SQL expressions to define business terminology, and text instructions only when other methods don't apply. The more structured context you provide through metadata and examples, the more accurately Genie can interpret questions and generate correct results.

Keep these guiding principles in mind as you build your Genie space:

* **Provide concise, well-documented datasets**: Quality table and column descriptions in Unity Catalog are critical for Genie accuracy. Resolve column ambiguities and pre-join or de-normalize tables using views or [metric views](/aws/en/metric-views/). Well-documented, simplified datasets improve Genie's ability to answer data questions accurately.
* **Prioritize SQL expressions and example SQL over text instructions**: Use SQL expressions to define business semantics like metrics and filters. Use example SQL to teach Genie how to handle common ambiguous prompts. Use text instructions only as a last resort when SQL expressions and examples cannot address the need. Structured definitions through SQL are more reliable and maintainable than plain text guidance.
* **Write clear, specific text instructions**: Avoid vague instructions. For example, instead of "Ask clarification questions when asked about sales," write "When users ask about sales metrics without specifying product name or sales channel, ask: To proceed with sales analysis, specify your product name and sales channel."
* **Avoid conflicting instructions**: Ensure consistency across all instruction types. For example, if text instructions specify rounding decimals to two digits, then example SQL queries must also round to two digits.

The following sections provide detailed recommendations for building spaces and resolving accuracy challenges.

### Start small[â](#start-small "Direct link to Start small")

Curating a Genie space is an iterative process. When creating a new space, start as small as possible, with minimal instructions and a limited set of questions to answer. Then, you can add as you iterate based on feedback and monitoring. This approach helps streamline creating and maintaining your space and allows you to curate it effectively in response to real user needs.

Use the following guidelines to help create a small Genie space:

* **Stay focused**: Include only the tables necessary to answer the questions you want the space to handle. Aim for five or fewer tables. The more focused your selection, the better. Keeping your space narrowly focused on a small amount of data is ideal, so limit the number of columns in your included tables.
* **Work within the 30 table limit**: Genie spaces support up to 30 tables or views. If your data topic requires more than 30 tables, prejoin related tables into views or [metric views](/aws/en/metric-views/) before adding them to your space. Metric views are particularly effective for Genie spaces because they pre-define metrics, dimensions, and aggregations. This approach helps you stay within the limit, simplifies your data model, and can improve Genie's response accuracy. See  [Manage data objects](/aws/en/genie/set-up#manage-data) for details on adding data objects to your space.
* **Plan to iterate**: Start with a minimal setup for your space, focusing on essential tables and basic instructions. Add more detailed guidance and examples as you refine the space over time, rather than aiming for perfection initially.
* **Build on well-annotated tables**: Genie uses Unity Catalog column names and descriptions to generate responses. Clear column names and descriptions help produce high-quality responses. Column descriptions should offer precise contextual information. Avoid ambiguous or unnecessary details. Inspect any AI-generated descriptions for accuracy and clarity, and use them only if they align with what you would manually provide.

### Have a domain expert define the space[â](#have-a-domain-expert-define-the-space "Direct link to Have a domain expert define the space")

An effective space creator needs to understand the data and the insights that can be gleaned from it. Data analysts who are proficient in SQL typically have the knowledge and skills to curate the space.

### Define the purpose of your space[â](#define-the-purpose-of-your-space "Direct link to Define the purpose of your space")

Identifying your space's specific audience and purpose helps you decide which data, instructions, and test questions to use. A space should answer questions for a particular topic and audience, not general questions across various domains. You can simplify your datasets by prejoining tables and removing unnecessary columns before adding data to a space. As you add data to your space, keep it tightly focused on the space's defined purpose. Hide any columns that might be confusing or unimportant. See [Hide or show relevant columns](/aws/en/genie/knowledge-store#show-hide-column).

### Add metadata and synonyms[â](#add-metadata-and-synonyms "Direct link to Add metadata and synonyms")

You can add column synonyms and custom descriptions to data in a Genie space. This metadata is scoped to your Genie space and does not overwrite metadata stored in Unity Catalog. Quality column descriptions and synonyms help Genie understand the column better, choose it for relevant questions, and write more accurate SQL. See [Edit column metadata](/aws/en/genie/knowledge-store#edit-column-metadata).

### Use Genie prompt matching[â](#use-genie-prompt-matching "Direct link to Use Genie prompt matching")

Prompt matching allows Genie to match values that are most relevant to the user's question and correct spelling issues in user prompts. This improves Genie's accuracy by helping it better match user prompts to the correct columns and values. Genie automatically provides prompt matching as you add tables to the space. You can manage which columns have prompt matching enabled. See  [Manage data objects](/aws/en/genie/set-up#manage-data) and [Build a knowledge store for more reliable Genie spaces](/aws/en/genie/knowledge-store).

### Provide focused examples and instructions[â](#provide-focused-examples-and-instructions "Direct link to Provide focused examples and instructions")

Genie spaces perform best with a limited, focused set of instructions. Databricks recommends leveraging example SQL queries to provide instructions in your space. Example SQL queries allow Genie to match user prompts to verified SQL queries and learn from examples to answer related questions. See  [Add example SQL queries and functions](/aws/en/genie/set-up#example-queries).

For context that should be applied globally in the Genie space, a small, well-organized set of plain text instructions can also help maintain relevance and improve response quality. Too many instructions can reduce effectiveness, especially in longer conversations, because Genie might struggle to prioritize the most important guidance. For details, see  [Provide instructions](/aws/en/genie/set-up#provide-instructions).

### Choose the right instruction type[â](#choose-the-right-instruction-type "Direct link to Choose the right instruction type")

Use the following guidelines to decide between SQL expressions, example SQL queries, and text instructions:

* **Use SQL expressions for common business terms**: When defining frequently used metrics, filters, or dimensions that represent standard business concepts, use SQL expressions in the knowledge store. SQL expressions are efficient, reusable definitions that help Genie understand your business logic. For example, use SQL expressions to define `revenue`, `active_customers`, `gross_margin`, or `recent_sales`. See [Define SQL expressions](/aws/en/genie/knowledge-store#sql-expressions).
* **Use example SQL queries for complex questions**: When addressing hard-to-interpret, multi-part, or complex questions, provide complete example SQL queries. These examples show Genie how to handle intricate query patterns and multi-step logic. For example, you might create SQL queries for prompts like "breakdown my team's performance" or "For customers who've only joined recently, what products are doing the best?". See  [Add example SQL queries and functions](/aws/en/genie/set-up#example-queries).
* **Use text instructions only as a last resort**: Text instructions should be used sparingly, only when SQL expressions and examples cannot address the need. Use text instructions for guidance that requires natural language explanation, such as "When users ask about customer performance without specifying a time range, ask them to clarify the time period" or "Always round percentages to two decimal places in summaries." Avoid using text instructions to define metrics, filters, or query patterns that can be expressed through SQL.

### Prompt Genie to ask clarification questions[â](#prompt-genie-to-ask-clarification-questions "Direct link to Prompt Genie to ask clarification questions")

To prompt Genie to ask clarification questions in certain scenarios, be explicit about when to ask for clarifications and how to follow up. Use clear, specific instructions that define both the triggering conditions and the expected clarification behavior.

For example, add the following type of instruction to your space:

> When users ask about sales performance breakdown but don't include time range, sales channel, or which KPIs in their prompt, you must ask a clarification question first to gather necessary information. For example: "Please specify the time range and sales channel you are looking for."

Structure your clarification instructions with these components:

* **Trigger condition**: Define what topics or scenarios require clarification (for example, "When users ask about X topic...")
* **Missing details**: Specify what information must be present (for example, "...but don't include Y details...")
* **Required action**: State that Genie must ask for clarification (for example, "...you must ask a clarification question first...")
* **Example clarification**: Provide the specific question Genie should ask (for example, "Please specify...")

Add clarification question instructions at the end of your general instructions to help Genie prioritize this behavior when responding to ambiguous questions.

### Customize summaries[â](#customize-summaries "Direct link to Customize summaries")

Genie provides natural language summaries alongside query results to help users understand the data. You can customize how Genie generates these summaries by adding specific instructions to your space's text instructions. Summary customization instructions apply to all responses in the space.

To customize summary behavior, add a dedicated section at the end of your text instructions with the heading "Instructions you must follow when providing summaries".

Example summary customization instructions:

> **Instructions you must follow when providing summaries**
>
> * Always respond in French when providing summaries
> * Cite the table and column names used in your analysis
> * Use bullet points to structure multi-part summaries
> * Include the date range covered in the results

note

* Only text instructions affect summary generation. SQL examples and SQL expressions don't influence how Genie creates summaries.
* Some customizations aren't available, such as controlling summary length and detail level.

### Test and adjust[â](#test-and-adjust "Direct link to Test and adjust")

You should be your space's first user. After you create a new space, start asking questions. Carefully examine the SQL generated in response to your questions. If Genie misinterprets the data, questions, or business jargon, you can intervene by editing the generated SQL or providing other specific instructions. Keep testing and editing until you're getting reliable responses.

After you've reviewed a question, you can add it as a benchmark question that you can use to test and score your space for overall accuracy systematically. You can use variations and different question phrasings to test Genie's responses. See [Use benchmarks in a Genie space](/aws/en/genie/benchmarks).

For ideas on fixing erroneous responses, see [Troubleshoot Genie spaces](/aws/en/genie/troubleshooting).

### Conduct user testing[â](#conduct-user-testing "Direct link to Conduct user testing")

After verifying response quality through testing, recruit a business user to try the Genie space. Use the following guidelines to provide a smooth user journey and collect feedback for ongoing improvement:

* Set expectations that their job is to help refine the space.
* Ask them to focus their testing on the specific topic and questions the space is designed to answer.
* If they receive an incorrect response, encourage users to add additional instructions and clarifications in the chat to refine the answer. When a correct response is provided, they should upvote the final query to minimize similar errors in future interactions.
* Tell users to upvote or downvote responses using the built-in feedback mechanism.
* Invite users to share additional feedback and unresolved questions directly with the space authors. Authors and editors can use feedback to refine instructions, examples, and trusted assets.

Consider providing training materials or a written document with guidelines for testing the space and providing feedback. Direct business users to [Use a Genie space to explore business data](/aws/en/genie/talk-to-genie) to help them start working with a new Genie space.

As business users test the space, users with at least CAN MANAGE permissions can see the questions they've asked on the **Monitoring** tab


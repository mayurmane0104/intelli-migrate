# Authoring Q&A - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/gen-bi-author-q-and-a.html](https://docs.aws.amazon.com/quick/latest/userguide/gen-bi-author-q-and-a.html)

---

## Converting to the Generative Q&A experience

            If you have existing topics, you can easily convert these to leverage our new
                generative capabilities. Navigate to a topic, and then choose
                    **Convert** next to the topic name. You will then be prompted
                to **Duplicate & Convert Topic** in a dialog box. We duplicate
                your topic for you so that the conversion to our beta experience does not impact
                your end users. Once you are satisfied with topic performance in the new experience,
                you can unshare the original topic and share the new one.

## Named entities

            Named entities are one of the most important components of topic curation. The
                information contained in named entities — specifically, the ordering of
                fields and their ranking — is what makes it possible to present contextual,
                multi-visual answers in response to even vague questions. Authors can find named
                entities by navigating to a topic, choosing the **Data** tab, and
                then choosing the **Named Entities**. From here, authors can
                preview or edit existing named entities, and create new ones.

Authors can configure the following facets of named entities:

- 
                    **Fields**: Choose a dataset, and then choose which fields from that dataset to include. This defines the scope of data that will be considered when using this named entity to answer enduser questions.
- 
                    **Field Rank and Presentation**: The relative rank of the dimensions and measures in a named entity determines how those fields are used when generating contextual, multi-visual answers. Note in the following demo that adjusting the relative rank of**Profit**so that it is higher than**Sales**leads to different data being displayed. By default, the order of fields in the table visual is the same as the field rank. However, you can control these two individually by turning off**Sync table view with field ranking**.
- 
                    **Show / Hide in Presentation**: Fields that are included in named entities can simultaneously be hidden from the tabular presentation of the named entity, while still providing additional context in other components of the answer.

## Measure aggregations

            Authors have fine-grained control over aggregated measures in topics. Across
                Quick Sight, measures are defaulted to `SUM`,unless they have custom
                aggregations defined in a calculated expression. To change this, navigate to the
                measure in the list of data fields, and specify a different default aggregation. You
                can also disallow aggregations, which will prevent them from being applied even if a
                user specifically asks for them. Lastly, you can specify that a measure is
                non-additive. This is useful for pre-computed metrics, such as percentages, which
                should not be re-combined in any way. Doing so will force `MEDIAN` or
                    `AVG` depending on your use case.
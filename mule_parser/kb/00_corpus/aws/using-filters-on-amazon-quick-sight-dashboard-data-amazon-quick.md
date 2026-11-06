# Using filters on Amazon Quick Sight dashboard data - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/filtering-dashboard-data.html](https://docs.aws.amazon.com/quick/latest/userguide/filtering-dashboard-data.html)

---

You can use filters to refine the data displayed in a visual. Filters are applied to the data before any aggregate functions. If you have multiple filters, all top-level filters apply together using AND. If the filters are grouped inside a top-level filter, the filters in the group apply using OR.

Amazon Quick Sight applies all of the enabled filters to the field. For example, suppose that
                there is one filter of `state = WA` and another filter of ```
sales >=
                    500
```
. In this case, the dataset contains only records that meet both of
                those criteria. If you disable one of these, only one filter applies. Take care that
                multiple filters applied to the same field aren't mutually exclusive.

## Viewing filters

                To see the existing filters, choose **Filter** on the element
                    settings menu, then choose to view filters. The filters display in the
                        **Applied filters** panel in order of creation, with the
                    oldest filter on top.

### Understanding filter icons in an Amazon Quick Sight dashboard

Filters in the **Applied filters** panel display icons to
                        indicate how they are scoped and whether they are enabled.

A filter that isn't enabled is grayed out, and you can't select its check box.

One of several scope icons displays to the right of the filter name to indicate the scope set on that filter. The scope icon resembled four boxes in a square. If all boxes are filled, the filter applies to all visuals on the analysis sheet. If only one box is filled, the filter applies to the selected visual only. If some boxes are filled, the filter applies to some of the visuals on the sheet, including the one currently selected.

The scope icons match the ones that display on the filter menu when you are choosing the scope for the filter.

### Viewing filter details in an Amazon Quick Sight dashboard

To see filter details, choose **Filter** at left. The
                        filter view retains your last selection. So when you open
                            **Filter**, you see either the **Applied
                            filters** or the **Edit filter** view.

In the **Applied filters** view, you can choose any
                        filter to view its details. The filters in this list can change depending on
                        the scope of the filter, and which visual you currently have
                        selected.

You can close the **Edit filter** view by choosing the
                        selector on the right. Doing this resets the **Filter**
                        view.
# Using visual field controls - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/using-visual-field-controls.html](https://docs.aws.amazon.com/quick/latest/userguide/using-visual-field-controls.html)

---

You can edit the fields used by a visual with user interface (UI) controls.

You can use these controls as follows:

- 
					Create a visual and assign fields to different elements on it by selecting fields in the **Fields list**pane, or dragging fields to field wells or drop targets.
- 
					Change the field associated with a visual element by dragging a field to a drop target or field well, or selecting a different field in a field well or on-visual editor. 
- 
					Change field aggregation or date granularity by using the field wells or the on-visual editors. 

The field wells, on-visual editors, and drop targets available on a specific visual depends on the visual type selected.

## Dragging fields to drop targets or field wells

				When you drag a field to either a drop target or field well, Amazon Quick provides you with information about whether the target element expects a measure or a dimension. Amazon Quick also provides you with information about whether that element is available for field assignment.

For example, when you drag a measure to the value drop target on a new single-measure line chart, you see the drop target color-coded green. That green color coding indicates that the drop target expects a measure. The drag label indicates that the target is available to add a field.

When you drag a dimension to the x-axis or color drop target on a new line chart, you see a label color-coded blue. That blue color coding indicates that the drop target expects a dimension. The drag label indicates that the target is available to add a field.

You can also drag a measure or dimension to a drop target on a line chart where the element is already associated with a field. In this case, the drag label indicates that you are replacing the field currently associated with the drop target.
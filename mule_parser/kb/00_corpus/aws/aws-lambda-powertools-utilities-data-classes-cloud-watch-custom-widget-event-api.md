# aws_lambda_powertools.utilities.data_classes.cloud_watch_custom_widget_event API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/cloud_watch_custom_widget_event.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/cloud_watch_custom_widget_event.html)

---

# Module `aws_lambda_powertools.utilities.data_classes.cloud_watch_custom_widget_event`

## Classes

- `class CloudWatchDashboardCustomWidgetEvent (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class CloudWatchDashboardCustomWidgetEvent(DictWrapper): """CloudWatch dashboard custom widget event You can use a Lambda function to create a custom widget on a CloudWatch dashboard. Documentation: ------------- - https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/add_custom_widget_dashboard_about.html """ @property def describe(self) -> bool: """Display widget documentation""" return bool(self.get("describe", False)) @property def widget_context(self) -> CloudWatchWidgetContext | None: """The widget context""" if self.get("widgetContext"): return CloudWatchWidgetContext(self["widgetContext"]) return None`CloudWatch dashboard custom widget event You can use a Lambda function to create a custom widget on a CloudWatch dashboard. ## Documentation:## Parameters- `data`- `dict[str, Any]`
- Lambda Event Source Event payload
- `json_deserializer`- `Callable`, optional
- function to deserialize `str`,`bytes`,`bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ### Ancestors- [DictWrapper](common.html#aws_lambda_powertools.utilities.data_classes.common.DictWrapper)
- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Instance variables- `prop describe : bool`
- 
## Expand source code`@property def describe(self) -> bool: """Display widget documentation""" return bool(self.get("describe", False))`Display widget documentation 
- `prop widget_context :`- [CloudWatchWidgetContext](#aws_lambda_powertools.utilities.data_classes.cloud_watch_custom_widget_event.CloudWatchWidgetContext)| None
- 
## Expand source code`@property def widget_context(self) -> CloudWatchWidgetContext | None: """The widget context""" if self.get("widgetContext"): return CloudWatchWidgetContext(self["widgetContext"]) return None`The widget context 
 ### Inherited members
- `class CloudWatchWidgetContext (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class CloudWatchWidgetContext(DictWrapper): @property def dashboard_name(self) -> str: """Get dashboard name, in which the widget is used""" return self["dashboardName"] @property def widget_id(self) -> str: """Get widget ID""" return self["widgetId"] @property def domain(self) -> str: """AWS domain name""" return self["domain"] @property def account_id(self) -> str: """Get AWS Account ID""" return self["accountId"] @property def locale(self) -> str: """Get locale language""" return self["locale"] @property def timezone(self) -> TimeZone: """Timezone information of the dashboard""" return TimeZone(self["timezone"]) @property def period(self) -> int: """The period shown on the dashboard""" return int(self["period"]) @property def is_auto_period(self) -> bool: """Whether auto period is enabled""" return bool(self["isAutoPeriod"]) @property def time_range(self) -> TimeRange: """The widget time range""" return TimeRange(self["timeRange"]) @property def theme(self) -> str: """The dashboard theme, i.e. 'light' or 'dark'""" return self["theme"] @property def link_charts(self) -> bool: """The widget is linked to other charts""" return bool(self["linkCharts"]) @property def title(self) -> str: """Get widget title""" return self["title"] @property def params(self) -> dict[str, Any]: """Get widget parameters""" return self["params"] @property def forms(self) -> dict[str, Any]: """Get widget form data""" return self["forms"]["all"] @property def height(self) -> int: """Get widget height""" return int(self["height"]) @property def width(self) -> int: """Get widget width""" return int(self["width"])`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
- Lambda Event Source Event payload
- `json_deserializer`- `Callable`, optional
- function to deserialize `str`,`bytes`,`bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ### Ancestors- [DictWrapper](common.html#aws_lambda_powertools.utilities.data_classes.common.DictWrapper)
- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Instance variables- `prop account_id : str`
- 
## Expand source code`@property def account_id(self) -> str: """Get AWS Account ID""" return self["accountId"]`Get AWS Account ID 
- `prop dashboard_name : str`
- 
## Expand source code`@property def dashboard_name(self) -> str: """Get dashboard name, in which the widget is used""" return self["dashboardName"]`Get dashboard name, in which the widget is used 
- `prop domain : str`
- 
## Expand source code`@property def domain(self) -> str: """AWS domain name""" return self["domain"]`AWS domain name 
- `prop forms : dict[str, Any]`
- 
## Expand source code`@property def forms(self) -> dict[str, Any]: """Get widget form data""" return self["forms"]["all"]`Get widget form data 
- `prop height : int`
- 
## Expand source code`@property def height(self) -> int: """Get widget height""" return int(self["height"])`Get widget height 
- `prop is_auto_period : bool`
- 
## Expand source code`@property def is_auto_period(self) -> bool: """Whether auto period is enabled""" return bool(self["isAutoPeriod"])`Whether auto period is enabled 
- `prop link_charts : bool`
- 
## Expand source code`@property def link_charts(self) -> bool: """The widget is linked to other charts""" return bool(self["linkCharts"])`The widget is linked to other charts 
- `prop locale : str`
- 
## Expand source code`@property def locale(self) -> str: """Get locale language""" return self["locale"]`Get locale language 
- `prop params : dict[str, Any]`
- 
## Expand source code`@property def params(self) -> dict[str, Any]: """Get widget parameters""" return self["params"]`Get widget parameters 
- `prop period : int`
- 
## Expand source code`@property def period(self) -> int: """The period shown on the dashboard""" return int(self["period"])`The period shown on the dashboard 
- `prop theme : str`
- 
## Expand source code`@property def theme(self) -> str: """The dashboard theme, i.e. 'light' or 'dark'""" return self["theme"]`The dashboard theme, i.e. 'light' or 'dark' 
- `prop time_range :`- [TimeRange](#aws_lambda_powertools.utilities.data_classes.cloud_watch_custom_widget_event.TimeRange)
- 
## Expand source code`@property def time_range(self) -> TimeRange: """The widget time range""" return TimeRange(self["timeRange"])`The widget time range 
- `prop timezone :`- [TimeZone](#aws_lambda_powertools.utilities.data_classes.cloud_watch_custom_widget_event.TimeZone)
- 
## Expand source code`@property def timezone(self) -> TimeZone: """Timezone information of the dashboard""" return TimeZone(self["timezone"])`Timezone information of the dashboard 
- `prop title : str`
- 
## Expand source code`@property def title(self) -> str: """Get widget title""" return self["title"]`Get widget title 
- `prop widget_id : str`
- 
## Expand source code`@property def widget_id(self) -> str: """Get widget ID""" return self["widgetId"]`Get widget ID 
- `prop width : int`
- 
## Expand source code`@property def width(self) -> int: """Get widget width""" return int(self["width"])`Get widget width 
 ### Inherited members
- `class TimeRange (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class TimeRange(DictWrapper): @property def mode(self) -> str: """The time range mode, i.e. 'relative' or 'absolute'""" return self["mode"] @property def start(self) -> int: """The start time within the time range""" return self["start"] @property def end(self) -> int: """The end time within the time range""" return self["end"] @property def relative_start(self) -> int | None: """The relative start time within the time range""" return self.get("relativeStart") @property def zoom_start(self) -> int | None: """The start time within the zoomed time range""" return (self.get("zoom") or {}).get("start") @property def zoom_end(self) -> int | None: """The end time within the zoomed time range""" return (self.get("zoom") or {}).get("end")`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
- Lambda Event Source Event payload
- `json_deserializer`- `Callable`, optional
- function to deserialize `str`,`bytes`,`bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ### Ancestors- [DictWrapper](common.html#aws_lambda_powertools.utilities.data_classes.common.DictWrapper)
- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Instance variables- `prop end : int`
- 
## Expand source code`@property def end(self) -> int: """The end time within the time range""" return self["end"]`The end time within the time range 
- `prop mode : str`
- 
## Expand source code`@property def mode(self) -> str: """The time range mode, i.e. 'relative' or 'absolute'""" return self["mode"]`The time range mode, i.e. 'relative' or 'absolute' 
- `prop relative_start : int | None`
- 
## Expand source code`@property def relative_start(self) -> int | None: """The relative start time within the time range""" return self.get("relativeStart")`The relative start time within the time range 
- `prop start : int`
- 
## Expand source code`@property def start(self) -> int: """The start time within the time range""" return self["start"]`The start time within the time range 
- `prop zoom_end : int | None`
- 
## Expand source code`@property def zoom_end(self) -> int | None: """The end time within the zoomed time range""" return (self.get("zoom") or {}).get("end")`The end time within the zoomed time range 
- `prop zoom_start : int | None`
- 
## Expand source code`@property def zoom_start(self) -> int | None: """The start time within the zoomed time range""" return (self.get("zoom") or {}).get("start")`The start time within the zoomed time range 
 ### Inherited members
- `class TimeZone (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class TimeZone(DictWrapper): @property def label(self) -> str: """The time range label. Either 'UTC' or 'Local'""" return self["label"] @property def offset_iso(self) -> str: """The time range offset in the format +/-00:00""" return self["offsetISO"] @property def offset_in_minutes(self) -> int: """The time range offset in minutes""" return int(self["offsetInMinutes"])`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
- Lambda Event Source Event payload
- `json_deserializer`- `Callable`, optional
- function to deserialize `str`,`bytes`,`bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ### Ancestors- [DictWrapper](common.html#aws_lambda_powertools.utilities.data_classes.common.DictWrapper)
- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Instance variables- `prop label : str`
- 
## Expand source code`@property def label(self) -> str: """The time range label. Either 'UTC' or 'Local'""" return self["label"]`The time range label. Either 'UTC' or 'Local' 
- `prop offset_in_minutes : int`
- 
## Expand source code`@property def offset_in_minutes(self) -> int: """The time range offset in minutes""" return int(self["offsetInMinutes"])`The time range offset in minutes 
- `prop offset_iso : str`
- 
## Expand source code`@property def offset_iso(self) -> str: """The time range offset in the format +/-00:00""" return self["offsetISO"]`The time range offset in the format +/-00:00 
 ### Inherited members
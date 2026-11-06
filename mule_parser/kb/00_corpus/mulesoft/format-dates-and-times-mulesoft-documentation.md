# Format Dates and Times | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-format-dates](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-format-dates)

---

```
%dw 2.0
output application/json
---
{
  formattedDate: |2020-10-01T23:57:59| as String {format: "uuuu-MM-dd"},
  formattedTime: |2020-10-01T23:57:59| as String {format: "KK:mm:ss a"},
  formattedDateTime: |2020-10-01T23:57:59| as String {format: "KK:mm:ss a, MMMM dd, uuuu"}
}
```
# Format Dates and Times

You can use DataWeave to change the format of date and time input.

## Change Date and Time Formats

You can combine formatting characters, such as `MM` and `dd`, to write supported date and time formats. The example uses the `as` operator to write the dates and times as a string.

## Create a Custom Date Format as a DataWeave Type

For multiple, similar conversions in your script, you can define a custom type as a directive in the header and set each date to that type. Names of DataWeave type are case-sensitive.

## Use Date and Time Formatting Characters

DataWeave supports the use of formatting characters, such as the `u` (for the year), `M`, and `d` in the date format `uuuu-MM-dd`. These characters are based on the Java 8 `java.time.format` package.

The following example formats the output of the `now` DataWeave function to show
supported letters:

```
%dw 2.0
var myDateTime = ("2020-11-10T13:44:12.283-08:00" as DateTime)
output application/json
---
{
    "dateTime" : myDateTime,
    "era-G" : myDateTime as String { format: "G"},
    "year-u" : myDateTime as String {format: "u"},
    "year-uu" : myDateTime as String {format: "uu"},
  //y is for use with the era (BCE or CE). Generally, use u, instead.
    "year-y" : myDateTime as String { format: "y"},
    "year-yy" : myDateTime as String { format: "yy"},
    "dayOfYear-D" : myDateTime as String { format: "D"},
    "monthOfYear-MMMM": myDateTime as String { format: "MMMM"},
    "monthOfYear-MMM": myDateTime as String { format: "MMM"},
    "monthOfYear-MM": myDateTime as String { format: "MM"},
    "monthOfYear-M": myDateTime as String { format: "M"},
    "monthOfYear-LL": myDateTime as String { format: "LL"},
    "monthOfYear-L": myDateTime as String { format: "L"},
    "dayOfMonth-d" : myDateTime as String {format: "d"},
    "quarterOfYear-qqq" : myDateTime as String {format: "qqq"},
    "quarterOfYear-qq" : myDateTime as String {format: "qq"},
    "quarterOfYear-q" : myDateTime as String {format: "q"},
    "quarterOfYear-QQQQ" : myDateTime as String {format: "QQQQ"},
    "quarterOfYear-QQQ" : myDateTime as String {format: "QQQ"},
    "quarterOfYear-QQ" : myDateTime as String {format: "QQ"},
    "quarterOfYear-Q" : myDateTime as String {format: "Q"},
  // Understand "Y" and "YY" thoroughly before using it.
    "weekBasedYear-YY" : myDateTime as String { format: "YY"},
    "weekBasedYear-Y" : myDateTime as String { format: "Y"},
    "weekInYear-w" : myDateTime as String {format: "w"},
    "weekInMonth-W" : myDateTime as String {format: "W"},
    "dayOfWeekAbbreviatedName-E" : myDateTime as String {format: "E"},
    "dayOfWeekFullName-EEEE" : myDateTime as String {format: "EEEE"},
    "localizedDayOfWeek-eeee" : myDateTime as String {format: "eeee"},
    "localizedDayOfWeek-eee" : myDateTime as String {format: "eee"},
    "localizedDayOfWeek-ee" : myDateTime as String {format: "ee"},
    "localizedDayOfWeek-e" : myDateTime as String {format: "e"},
    "localizedDayOfWeek-cccc" : myDateTime as String {format: "cccc"},
    "localizedDayOfWeek-ccc" : myDateTime as String {format: "ccc"},
    "localizedDayOfWeek-c" : myDateTime as String {format: "c"},
    "weekOfMonth-F" : myDateTime as String {format: "F"},
    "amORpm-a" : myDateTime as String {format: "a"},
  // "h" outputs 12 o'clock as 12. Other hours match "K" output.
    "hourOfDay1to12-h" : myDateTime as String {format: "h"},
  // "K" outputs 12 o'clock as 0. Other hours match "h" output.
    "hourOfDay0to11-K" : myDateTime as String {format: "K"},
    "clockHourOfAmPm-k" : myDateTime as String {format: "k"},
    "hourOfDay0to23-H" : myDateTime as String {format: "H"},
    "minuteOfHour-m" : myDateTime as String {format: "m"},
    "secondOfMinute-s" : myDateTime as String {format: "s"},
    "fractionOfSecond-S" : myDateTime as String {format: "S"},
    "millisecondOfDay-A" : myDateTime as String {format: "A"},
    "nanosecondCountOfSecond-n" : myDateTime as String {format: "n"},
    "nanosecondCountOfDay-N" : myDateTime as String {format: "N"},
    "timeZoneID-VV" : myDateTime as String {format: "VV"},
    "timeZoneName-zz" : myDateTime as String {format: "zz"},
    "localizedZoneOffset-zzz" : myDateTime as String {format: "zzz"},
    "localizedZoneOffset-O" : myDateTime as String {format: "O"},
    "timeZoneOffsetZforZero-XXX" : myDateTime as String {format: "XXX"},
    "timeZoneOffsetZforZero-XX" : myDateTime as String {format: "XX"},
    "timeZoneOffsetZforZero-X" : myDateTime as String {format: "X"},
    "timeZoneOffset-xxx" : myDateTime as String {format: "xxx"},
    "timeZoneOffset-xx" : myDateTime as String {format: "xx"},
    "timeZoneOffset-x" : myDateTime as String {format: "x"},
    "timeZoneOffset-Z" : myDateTime as String {format: "Z"}
 }
```
Notice the use of the syntax to format the date or time.

```
{
  "dateTime": "2020-11-10T13:44:12.283-08:00",
  "era-G": "AD",
  "year-u": "2020",
  "year-uu": "20",
  "year-y": "2020",
  "year-yy": "20",
  "dayOfYear-D": "315",
  "monthOfYear-MMMM": "November",
  "monthOfYear-MMM": "Nov",
  "monthOfYear-MM": "11",
  "monthOfYear-M": "11",
  "monthOfYear-LL": "11",
  "monthOfYear-L": "11",
  "dayOfMonth-d": "10",
  "quarterOfYear-qqq": "4",
  "quarterOfYear-qq": "04",
  "quarterOfYear-q": "4",
  "quarterOfYear-QQQQ": "4th quarter",
  "quarterOfYear-QQQ": "Q4",
  "quarterOfYear-QQ": "04",
  "quarterOfYear-Q": "4",
  "weekBasedYear-YY": "20",
  "weekBasedYear-Y": "2020",
  "weekInYear-w": "46",
  "weekInMonth-W": "2",
  "dayOfWeekAbbreviatedName-E": "Tue",
  "dayOfWeekFullName-EEEE": "Tuesday",
  "localizedDayOfWeek-eeee": "Tuesday",
  "localizedDayOfWeek-eee": "Tue",
  "localizedDayOfWeek-ee": "03",
  "localizedDayOfWeek-e": "3",
  "localizedDayOfWeek-cccc": "Tuesday",
  "localizedDayOfWeek-ccc": "Tue",
  "localizedDayOfWeek-c": "3",
  "weekOfMonth-F": "3",
  "amORpm-a": "PM",
  "hourOfDay1to12-h": "1",
  "hourOfDay0to11-K": "1",
  "clockHourOfAmPm-k": "13",
  "hourOfDay0to23-H": "13",
  "minuteOfHour-m": "44",
  "secondOfMinute-s": "12",
  "fractionOfSecond-S": "2",
  "millisecondOfDay-A": "49452283",
  "nanosecondCountOfSecond-n": "283000000",
  "nanosecondCountOfDay-N": "49452283000000",
  "timeZoneID-VV": "-08:00",
  "timeZoneName-zz": "-08:00",
  "localizedZoneOffset-zzz": "-08:00",
  "localizedZoneOffset-O": "GMT-8",
  "timeZoneOffsetZforZero-XXX": "-08:00",
  "timeZoneOffsetZforZero-XX": "-0800",
  "timeZoneOffsetZforZero-X": "-08",
  "timeZoneOffset-xxx": "-08:00",
  "timeZoneOffset-xx": "-0800",
  "timeZoneOffset-x": "-08",
  "timeZoneOffset-Z": "-0800"
}
```
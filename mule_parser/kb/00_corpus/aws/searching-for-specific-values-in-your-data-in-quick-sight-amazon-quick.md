# Searching for specific values in your data in Quick Sight - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/search-filter.html](https://docs.aws.amazon.com/quick/latest/userguide/search-filter.html)

---

When filtering your visual data, previewing anomalies, or using list or dropdown controls in a dashboard, you can quickly search for values that interest you.

You can search for specific values or all values that contain a specific
                    search query. For example, searching for *al*
                    in a list of U.S. states returns **Al**abama,
                        **Al**aska, and C**al**ifornia.

You can also use wildcard search to search for all values that match a
                    specific character pattern. For example, you can search for all U.S. states that
                    end with the letters *ia* and narrow the
                    results down to California, Georgia, Pennsylvania, Virginia, and West
                    Virginia.

**To search for values in a filter or control**,
                    enter a search query in the search bar. 

## Using wildcard search

                    The following wildcard characters can be used to find values in Quick Sight filters, list and dropdown controls, and anomaly previews.

- 
                            *****- Use an asterisk symbol to search for values that match zero to many characters in a specific position.
- 
                            **?**- Use a question mark to match a single character in a specific position.
- 
                            **\**- Use a backslash to escape the*****,**?**, or**\**wildcard characters and search for them in your query. For example, you can search for phrases that end with a question mark.

Following are examples of how supported wildcard characters can be used in a Quick Sight search query.

- 
                            `al`- This query searches for all values with`al`and returns Alabama, Alaska, and California.
- 
                            `al*`- This query searches for all values that begin with`al`and end with zero to multiple characters. It returns Alabama, and Alaska in a list of U.S. states.
- 
                            `*ia`- This query searches for all values that begin with zero to multiple characters and end with letters`ia`. It returns California, Georgia, Pennsylvania, Virginia, and West Virginia.
- 
                            `*al*`- This query searches for all values with zero to multiple characters before and after the letters`al`. It returns Alabama, Alaska, and California.
- 
                            `a?a?a?a`- This query searches for all values with a single character in the exact positions between the`a`letters. It returns Alabama.
- 
                            `a?a*a`- This query searches for all values with a single character between the first two`a`letters and multiple characters between the second two`a`letters. It returns Alabama and Alaska.
- 
                            `How*\?`- This query searches for values that begin with`How`, followed by zero to multiple characters, and end with a question mark. The backslash (\) in this query informs Quick Sight to search for question marks in each value, rather than use the question mark symbol as a wildcard character. This query returns the questions, How are you? and, How is this possible?
- 
                            `\**`- This query searches for values that begin with an asterisk and are followed by zero to multiple characters. The backslash (\) in this query informs Quick Sight to search for an actual asterisk in the values, rather than use the asterisk symbol as a wildcard character. This query returns values such as *all, *above, and *below.
- 
                            `\\*`- This query searches for values with a backslash, followed by zero to multiple characters. The first backslash (\) in this query informs Quick Sight to search for the second backslash (\) in each value, rather than use the backslash symbol as a wildcard character. This query returns results such as \Home.
- 
                            `???`- This query searches for values that contain three characters. It returns values such as ant, bug, and car.
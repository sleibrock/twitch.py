Frequently Asked Questions
==========================

Nothing here yet!

## Why don't certain streams show up at all?

I had this problem for a while, after tinkering around, it turns out the issue 
is Twitch's API with the 'limit' field. Anything less than 20 usually fails to 
retrieve most streams properly, so I set the DEFAULT_LIMIT to 20 to make up for 
this issue.


#Q16-print the following pattern
"""
* * * * *
 * * * *
  * * *
   * *
    *   """

for i in range(4,0,-1):
    spaces=5-i
    stars=i*"* "
    print(" "* spaces+stars)
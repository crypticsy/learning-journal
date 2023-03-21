<h4> RegEx Functions </h4>

The <code>re</code> module offers a set of functions that allows us to search a string for a match:

<table style="width:100%;text-align: justify;">
  <tr>
    <th>Function</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>findall</td>
    <td>Returns a list containing all matches</td>
  </tr>
  <tr>
    <td>search</td>
    <td>Returns a Match object if there is a match anywhere in the string</td>
  </tr>
  <tr>
    <td>split</td>
    <td>Returns a list where the string has been split at each match</td>
  </tr>
  <tr>
    <td>sub</td>
    <td>Replaces one or many matches with a string</td>
  </tr>
</table>

<hr/>

<h4>Metacharacters</h4>
<p>Metacharacters are characters with a special meaning:</p>
<table style="width:100%;text-align: justify;">
  <tr>
    <th>Character</th>
    <th>Description</th>
    <th>Example</th>
  </tr>
  <tr>
    <td>[]</td>
    <td>Matches a set of characters in the listed set</td>
    <td>&quot;[a-m]&quot;</td>
  </tr>
  <tr>
    <td>\</td>
    <td>Signals a special sequence (can also be used to escape special characters)</td>
    <td>&quot;\d&quot;</td>
  </tr>
  <tr>
    <td>.</td>
    <td>Any character (except newline character)</td>
    <td>&quot;he..o&quot;</td>
  </tr>
  <tr>
    <td>^</td>
    <td>Starts with</td>
    <td>&quot;^hello&quot;</td>
  </tr>
  <tr>
    <td>$</td>
    <td>Ends with</td>
    <td>&quot;world$&quot;</td>
  </tr>
  <tr>
    <td>*</td>
    <td>Zero or more occurrences</td>
    <td>&quot;aix*&quot;</td>
  </tr>
  <tr>
    <td>*?</td>
    <td>Zero or more occurrences (non-greedy)</td>
    <td>&quot;aix*?&quot;</td>
  </tr>
  <tr>
    <td>+</td>
    <td>One or more occurrences</td>
    <td>&quot;aix+&quot;</td>
  </tr>
  <tr>
    <td>+?</td>
    <td>One or more occurrences (non-greedy)</td>
    <td>&quot;aix+?&quot;</td>
  </tr>
  <tr>
    <td>{}</td>
    <td>Exactly the specified number of occurrences</td>
    <td>&quot;al{2}&quot;</td>
  </tr>
  <tr>
    <td>|</td>
    <td>Either or</td>
    <td>&quot;falls|stays&quot;</td>
  </tr>
  <tr>
    <td>()</td>
    <td>Capture and group</td>
    <td></td>
  </tr>
</table>

<hr/>

<h4>Special Sequences</h4>

A special sequence is a <code>\\</code> followed by one of the characters in the list below, and has a special meaning:

<table style="width:100%;text-align: justify;">
    <tr>
        <th>Character</th>
        <th>Description</th>
        <th>Example</th>
    </tr>
    <tr>
        <td>\A</td>
        <td>Returns a match if the specified characters are at the beginning of the string</td>
        <td>&quot;\AThe&quot;</td>
    </tr>
    <tr>
        <td>\b</td>
        <td>Returns a match where the specified characters are at the beginning or at the end of a word</td>
        <td>r&quot;\bain&quot;<br>r&quot;ain\b&quot;</td>
    </tr>
    <tr>
        <td>\B</td>
        <td>Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word</td>
        <td>r&quot;\Bain&quot;<br>r&quot;ain\B&quot;</td>
    </tr>
    <tr>
        <td>\d</td>
        <td>Returns a match where the string contains digits (numbers from 0-9)</td>
        <td>&quot;\d&quot;</td>
    </tr>
    <tr>
        <td>\D</td>
        <td>Returns a match where the string DOES NOT contain digits</td>
        <td>&quot;\D&quot;</td>
    </tr>
    <tr>
        <td>\s</td>
        <td>Returns a match where the string contains a white space character</td>
        <td>&quot;\s&quot;</td>
    </tr>
    <tr>
        <td>\S</td>
        <td>Returns a match where the string DOES NOT contain a white space character</td>
        <td>&quot;\S&quot;</td>
    </tr>
    <tr>
        <td>\w</td>
        <td>Returns a match where the string contains any word characters (characters from 
        a to Z, digits from 0-9, and the underscore _ character)</td>
        <td>&quot;\w&quot;</td>
    </tr>
    <tr>
        <td>\W</td>
        <td>Returns a match where the string DOES NOT contain any word characters</td>
        <td>&quot;\W&quot;</td>
    </tr>
    <tr>
        <td>\Z</td>
        <td>Returns a match if the specified characters are at the end of the string</td>
        <td>&quot;Spain\Z&quot;</td>
    </tr>
</table>

<hr/>

<h4>Sets</h4>
<p>A set is a set of characters inside a pair of square brackets [] with a special meaning:</p>
<table style="width:100%;text-align: justify;">
    <tr>
        <th>Set</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>[arn]</td>
        <td>Returns a match where one of the specified characters (a, r, or n) are present</td>
    </tr>
    <tr>
        <td>[a-n]</td>
        <td>Returns a match for any lower case character, alphabetically between a and n</td>
    </tr>
    <tr>
        <td>[^arn]</td>
        <td>Returns a match for any character EXCEPT a, r, and n</td>
    </tr>
    <tr>
        <td>[0123]</td>
        <td>Returns a match where any of the specified digits (0, 1, 2, or 3) are present</td>
    </tr>
    <tr>
        <td>[0-9]</td>
        <td>Returns a match for any digit between 0 and 9</td>
    </tr>
    <tr>
        <td>[0-5][0-9]</td>
        <td>Returns a match for any two-digit numbers from 00 and 59</td>
    </tr>
    <tr>
        <td>[a-zA-Z]</td>
        <td>Returns a match for any character alphabetically between a and z, lower case OR upper case</td>
    </tr>
    <tr>
        <td>[+]</td>
        <td>In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string</td>
    </tr>
</table>

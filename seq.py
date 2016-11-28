{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Excercises for Day 4: Sequences\n",
    "\n",
    "[4.1 Strings](#4.1)\n",
    "\n",
    "[4.2 Lists](#4.2)\n",
    "\n",
    "[4.3 Dictionaries](#4.3)\n",
    "\n",
    "[4.4 The _collections_ module](#4.4)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4.1 Strings\n",
    "<a id='4.1'></a>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4.1.1\n",
    "Define a function that splits a text into sentences (on \".\", \"!\", \"?\", etc.)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def mondatokra(szoveg):\n",
    "    mondatok = []\n",
    "    for darab1 in szoveg.split('.'):\n",
    "        for darab2 in darab1.split('!'):\n",
    "            for darab3 in darab2.split('?'):\n",
    "                if darab3:\n",
    "                    mondatok.append(darab3)\n",
    "    return mondatok"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def mondatokra(szoveg):\n",
    "    mondatok = []\n",
    "    for punct in \".?\":\n",
    "        szoveg = szoveg.strip().replace(punct, '!')\n",
    "    for mondat in szoveg.split('!'):\n",
    "        if mondat.strip():\n",
    "            mondatok.append(mondat.strip())\n",
    "    return mondatok"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "szoveg = open('data/sample_text.txt').read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "mondatokra(szoveg)[-3:]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Define a function that splits sentences into words, and strips punctuation marks (\",\", \";\", etc.) from edges of words."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def szavakra(mondat):\n",
    "    szavak = mondat.split()\n",
    "    strippelt_szavak = []\n",
    "    for szo in szavak:\n",
    "        strippelt_szavak.append(szo.strip(\",;:()\"))\n",
    "    return strippelt_szavak"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use the last two functions in one that takes a filename as its argument and returns the text in the file as a list of lists. Test it on the file \"data/sample_text.txt\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def feldolgoz(fajl):\n",
    "    kimenet = []\n",
    "    szoveg = open(fajl).read()\n",
    "    for mondat in mondatokra(szoveg):\n",
    "        szavak = szavakra(mondat)\n",
    "        kimenet.append(szavak)\n",
    "    return kimenet"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "adat = feldolgoz('Sequences/data/sample_text.txt')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "adat[:3]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4.1.2\n",
    "Use the functions defined in __4.1.1__ and define a function that goes through a text and replaces all proper names (capitalized words not at the beginning of a sentence) with \"Joe\". Print the first few sentences to test your solution."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def joe(fajl):\n",
    "    kimenet = []\n",
    "    adat = feldolgoz(fajl)\n",
    "    for mondat in adat:\n",
    "        uj_mondat = []\n",
    "        uj_mondat.append(mondat[0])\n",
    "        for szo in mondat[1:]:\n",
    "            if szo.istitle():\n",
    "                uj_mondat.append(\"Joe\")\n",
    "            else:\n",
    "                uj_mondat.append(szo)\n",
    "        kimenet.append(uj_mondat)\n",
    "    return kimenet\n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[['Nevertheless', 'a', 'wholly', 'remarkable', 'book'],\n",
       " ['In',\n",
       "  'fact',\n",
       "  'it',\n",
       "  'was',\n",
       "  'probably',\n",
       "  'the',\n",
       "  'most',\n",
       "  'remarkable',\n",
       "  'book',\n",
       "  'ever',\n",
       "  'to',\n",
       "  'come',\n",
       "  'out',\n",
       "  'of',\n",
       "  'the',\n",
       "  'great',\n",
       "  'publishing',\n",
       "  'houses',\n",
       "  'of',\n",
       "  'Joe',\n",
       "  'Joe',\n",
       "  'of',\n",
       "  'which',\n",
       "  'no',\n",
       "  'Joe',\n",
       "  'had',\n",
       "  'ever',\n",
       "  'heard',\n",
       "  'either'],\n",
       " ['Not',\n",
       "  'only',\n",
       "  'is',\n",
       "  'it',\n",
       "  'a',\n",
       "  'wholly',\n",
       "  'remarkable',\n",
       "  'book',\n",
       "  'it',\n",
       "  'is',\n",
       "  'also',\n",
       "  'a',\n",
       "  'highly',\n",
       "  'successful',\n",
       "  'one',\n",
       "  'more',\n",
       "  'popular',\n",
       "  'than',\n",
       "  'the',\n",
       "  'Joe',\n",
       "  'Joe',\n",
       "  'Joe',\n",
       "  'Joe',\n",
       "  'better',\n",
       "  'selling',\n",
       "  'than',\n",
       "  'Joe',\n",
       "  'Joe',\n",
       "  'Joe',\n",
       "  'to',\n",
       "  'do',\n",
       "  'in',\n",
       "  'Joe',\n",
       "  'Joe',\n",
       "  'and',\n",
       "  'more',\n",
       "  'controversial',\n",
       "  'than',\n",
       "  'Joe',\n",
       "  \"Colluphid's\",\n",
       "  'trilogy',\n",
       "  'of',\n",
       "  'philosophical',\n",
       "  'blockbusters',\n",
       "  'Joe',\n",
       "  'Joe',\n",
       "  'Joe',\n",
       "  'Joe',\n",
       "  'Joe',\n",
       "  'Joe',\n",
       "  'of',\n",
       "  \"God's\",\n",
       "  'Joe',\n",
       "  'Joe',\n",
       "  'and',\n",
       "  'Joe',\n",
       "  'is',\n",
       "  'this',\n",
       "  'Joe',\n",
       "  'Joe',\n",
       "  'Joe']]"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "joe('Sequences/data/sample_text.txt')[-3:]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4.1.3\n",
    "Load the sample text using your function from __4.1.1__ and create a game where the user is shown a half of a word in a small context (e.g. \"_Many solu\\*\\*\\*\\*\\* were suggested_\") and has to guess the full word (don't worry about randomization, your solution can come up with the same questions every time)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4.2 Lists\n",
    "<a id='4.2'></a>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4.2.1\n",
    "Define a function that takes as its input a list of $n$ lists of $n$ numbers (a square matrix) and decides if it is symmetric (i.e. $A[i,j] == A[j,i]$ for all $i, j$)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def is_symmetric(matrix):\n",
    "    n = len(matrix)\n",
    "    for i in range(n):\n",
    "        for j in range(n):\n",
    "            ... matrix[i][j] ...\n",
    "            ..."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "test_matrix1 = [[1,2], [3,4]]\n",
    "test_matrix2 = [[1,2], [2,1]]\n",
    "print is_symmetric(test_matrix1)\n",
    "print is_symmetric(test_matrix2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4.2.2\n",
    "Define a function that takes a list containing lists of equal length (i.e. a table of size $n\\times k$) and \"transposes\" it, creating a table of size $k\\times n$."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def transpose(matrix):\n",
    "    n = len(matrix)\n",
    "    k = len(matrix[0])\n",
    "    new_matrix = []\n",
    "    for i in range(k):\n",
    "        new_row = []\n",
    "        for old_row in matrix:\n",
    "            new_row.append(old_row[i])\n",
    "        new_matrix.append(new_row)\n",
    "    return new_matrix\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4.2.3\n",
    "Redo 4.2.3 using nested list comprehension!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def transpose(matrix):\n",
    "    n = len(matrix)\n",
    "    m = len(matrix[0])\n",
    "    return [[matrix[i][j] for i in range(n)] for j in range(m)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "test_matrix = [[1,2,3], [4,5,6]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "transpose(test_matrix)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4.2.4"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Define a function that takes a list and string, then returns all elements that start with the string, along with their indices in the list."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4.3 Dictionaries\n",
    "<a id='4.3'></a>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4.3.1\n",
    "Use a dictionary to count words in our sample text (use your text processing functions!). Then print the most common words, along with their frequencies!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4.3.2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Define function that performs the factorial operation ($n!$) but caches all results so that each call requires the least possible number of multiplications."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4.3.3\n",
    "Read the dataset in \"data/movies.tsv\" and store it in a dictionary whose keys are genres and the values are list of tuples of title and year"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def process_data(fn):\n",
    "    data = {}\n",
    "    f = open(fn)\n",
    "    for line in f:\n",
    "        title, year, genres = line.strip().split('\\t')\n",
    "        title = title.strip()\n",
    "        year = int(year)\n",
    "        genres = genres.split(\",\")\n",
    "        for genre in genres:\n",
    "            if genre not in data:\n",
    "                data[genre] = []\n",
    "            data[genre].append((title, year))\n",
    "    return data        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "data = process_data(\"data/movies.tsv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "data['horror'][:5]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4.3.4\n",
    "Process the movies dataset (the original file or the dictionary built in __4.3.3__) and build a dictionary that indexes movies by the first letter of the title. Then create a small interface for querying (using the input function)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4.3.5\n",
    "Build an incremental search of movie titles: users should be able to narrow the set of movies with every character they type. You may create deeply nested dictionaries beforehand or process the data on-the-fly."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def build_index(data):\n",
    "    letter_index = {}\n",
    "    for movie in data:\n",
    "        title = movie[0]\n",
    "        try:\n",
    "            a, b, c = title[:3]\n",
    "        except ValueError:\n",
    "            print \"skipping: {0}\".format(title)\n",
    "            continue\n",
    "        if a not in letter_index:\n",
    "            letter_index[a] = {}\n",
    "        if b not in letter_index[a]:\n",
    "            letter_index[a][b] = {}\n",
    "        if c not in letter_index[a][b]:\n",
    "            letter_index[a][b][c] = []\n",
    "        letter_index[a][b][c].append(movie)\n",
    "    return letter_index\n",
    "\n",
    "def search(fn):\n",
    "    data = [(title.strip(), int(year), genres.split(','))\n",
    "            for title, year, genres in [line.strip().split('\\t')\n",
    "                                        for line in open(fn)]]\n",
    "    letter_index = build_index(data)\n",
    "    letter1 = raw_input()\n",
    "    print letter_index[letter1]\n",
    "    letter2 = raw_input()\n",
    "    print letter_index[letter1][letter2]\n",
    "    letter3 = raw_input()\n",
    "    print letter_index[letter1][letter2][letter3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def unify_dicts(dict1, dict2):\n",
    "    dict3 = {}\n",
    "    dict3.update(dict1)\n",
    "    for key, value in dict2.items():\n",
    "        if key not in dict3:\n",
    "            dict3[key] = value\n",
    "        else:\n",
    "            if not isinstance(dict3[key], dict):\n",
    "                dict3[key] = value\n",
    "            else:\n",
    "                dict3[key] = unify_dicts(dict3[key], value)\n",
    "    return dict3\n",
    "\n",
    "def get_letter_dict(title, movie):\n",
    "    if not title:\n",
    "        return {'@': movie}\n",
    "    else:\n",
    "        return {title[0]: get_letter_dict(title[1:], movie)}\n",
    "    \n",
    "def build_index(data):\n",
    "    letter_index = {}\n",
    "    for movie in data:\n",
    "        title = movie[0]\n",
    "        d = get_letter_dict(title, movie)\n",
    "        letter_index = unify_dicts(letter_index, d)\n",
    "    return letter_index\n",
    "\n",
    "def search(fn):\n",
    "    data = [(title.strip(), int(year), genres.split(','))\n",
    "            for title, year, genres in [line.strip().split('\\t')\n",
    "                                        for line in open(fn)]]\n",
    "    \n",
    "    letter_index = build_index(data)\n",
    "    letter = raw_input()\n",
    "    curr_dict = letter_index[letter]\n",
    "    while True:\n",
    "        print curr_dict\n",
    "        if '@' in curr_dict:\n",
    "            print curr_dict['@']\n",
    "            break\n",
    "        else:\n",
    "            letter = raw_input()\n",
    "            if letter not in curr_dict:\n",
    "                print 'not found :('\n",
    "                break\n",
    "            curr_dict = curr_dict[letter]\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "search(\"data/movies.tsv\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4.4 The _collections_ module\n",
    "<a id='4.4'></a>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4.4.1\n",
    "Modify the word counter in __4.3.1__ so that it uses a defaultdict."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4.4.2\n",
    "Modify the word counter in __4.4.1__ so that it uses a Counter."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4.4.3\n",
    "Define a function that queries users for their last name, first name, year of birth, and hobby, and populates an OrderedDict whose keys are the last names and values are dictionaries with four keys each. If a second person with the same last name is encountered, both should now have keys of the form \"lastname_firstname\". If the same person is encountered multiple times, his/her data should be updated. Then test the solution of someone else and ask her to test yours."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def query():\n",
    "    last_name = raw_input()\n",
    "    first_name = raw_input()\n",
    "    year = int(raw_input())\n",
    "    hobby = raw_input()\n",
    "    return last_name, first_name, year, hobby\n",
    "\n",
    "from collections import OrderedDict\n",
    "data = OrderedDict()\n",
    "while True:\n",
    "    last_name, first_name, year, hobby = query()\n",
    "    full_name = \"{0}_{1}\".format(last_name, first_name)\n",
    "    if last_name not in data:\n",
    "        if full_name in data:\n",
    "            data[full_name] = (first_name, year, hobby)\n",
    "        else:\n",
    "            data[last_name] = (first_name, year, hobby)\n",
    "             \n",
    "    else:\n",
    "        data[full_name] = (first_name, year, hobby)\n",
    "        first_guy = data[last_name]\n",
    "        first_key = \"{0}_{1}\".format(last_name, first_guy[0])\n",
    "        data[first_key] = first_guy\n",
    "        del data[last_name]\n",
    "    print data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4.4.4\n",
    "Convert the database built in __4.4.3__ into a list of namedtuples."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python [default]",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}

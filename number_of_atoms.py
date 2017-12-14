# python3
# Given a chemical formula (given as a string), return the count of each atom.

# An atomic element always starts with an uppercase character, then zero or more lowercase letters,
# representing the name.

# 1 or more digits representing the count of that element may follow if the count is greater than 1.
# If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.

# Two formulas concatenated together produce another formula. For example, H2O2He3Mg4 is also a formula.

# A formula placed in parentheses, and a count (optionally added) is also a formula.
# For example, (H2O2) and (H2O2)3 are formulas.

# Given a formula, output the count of all elements as a string in the following form: the first name (in sorted order),
# followed by its count (if that count is more than 1), followed by the second name (in sorted order),
# followed by its count (if that count is more than 1), and so on.

# Example 1:
# Input:
# formula = "H2O"
# Output: "H2O"
# Explanation:
# The count of elements are {'H': 2, 'O': 1}.
# Example 2:
# Input:
# formula = "Mg(OH)2"
# Output: "H2MgO2"
# Explanation:
# The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
# Example 3:
# Input:
# formula = "K4(ON(SO3)2)2"
# Output: "K4N2O14S4"
# Explanation:
# The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
# Note:

# All atom names consist of lowercase letters, except for the first character which is uppercase.
# The length of formula will be in the range [1, 1000].
# formula will only consist of letters, digits, and round parentheses, and is a valid formula as defined in the problem.


# My solution
class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        uppercaseletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lowercaseletters = uppercaseletters.lower()
        digits = '0123456789'
        formula = '(' + formula + ')'
        all_sub = []
        i = 0
        while i < len(formula):
            if formula[i] == '(':
                all_sub.append({})
                i += 1
            elif formula[i] in uppercaseletters:
                # find the current atom
                j = i + 1
                cur = formula[i]
                while j < len(formula):
                    if formula[j] in lowercaseletters:
                        cur += formula[j]
                    else:
                        break
                    j += 1
                # find the count of the current atom
                count = ''
                while j < len(formula):
                    if formula[j] in digits:
                        count += formula[j]
                    else:
                        break
                    j += 1
                if count == '':
                    count = 1
                else:
                    count = int(count)
                # add the current atom
                if cur in all_sub[-1]:
                    all_sub[-1][cur] += count
                else:
                    all_sub[-1][cur] = count
                i = j
            elif formula[i] == ')':
                # find the count of the current atoms
                j = i + 1
                count = ''
                while j < len(formula):
                    if formula[j] in digits:
                        count += formula[j]
                    else:
                        break
                    j += 1
                cur = all_sub.pop()
                if count != '':
                    count = int(count)
                    for it in cur.keys():
                        cur[it] *= count
                if all_sub != []:
                    pre = all_sub.pop()
                    for it in pre.keys():
                        if it in cur:
                            cur[it] += pre[it]
                        else:
                            cur[it] = pre[it]
                all_sub.append(cur)
                i = j
            else:
                i += 1
        out = all_sub.pop()
        while all_sub:
            cur = all_sub
            for it in cur.keys:
                if it in out:
                    out[it] += cur[it]
                else:
                    out[it] = cur[it]
        list_keys = sorted(out.keys())
        out_str = ''
        for it in list_keys:
            if out[it] != 1:
                out_str += (it + str(out[it]))
            else:
                out_str += it

        return out_str










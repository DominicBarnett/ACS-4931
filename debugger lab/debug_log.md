# Debug Log

**Explain how you used the VSCode debugger tools to uncover the bugs in Exercise 7. Be specific. What breakpoints did you set? Where did you step to? What made you realize the error?**

_Example: I set a breakpoint on line 5 and stepped until line 12. There, I discovered that the `x` variable had a value of `-3`, whereas it should have had a value of `7`. That made me realize that we should be adding the two numbers `x` and `y`, instead of subtracting._

1. Initial thoughts and ideas: After glossing over the code, I ran it with `python3 exercise7.py` and was expecting to see: "fantastic, I guess programming is fantastic." However, the output was just "fantastic". Based on this behavior, I have a hypothsis that the code is not saving the sentence properly in the `remainder_of_sentence` variable.

2. Using the debugging tool: I placed a breakpoint on line 1 and used step over and step into to see exactly what was going on line by line. The recursive case looked normal with a sentence value of `sentence: 'okay, I guess programming is okay.` but quickly after, I noticed that `remainder_of_sentence` returned as an empty string. This is a huge issue because `return replace_str + replace_substring(remainder_of_sentence, start_str, replace_str)` is supposed to return the remainder of the sentence with the replaced string and proves that my theory is correct. But how do we fix this?

3. Fixing the bug: After looking at it for a bit, I realized that `remainder_of_sentence = start_str[len(start_str):]` should be replaced with `remainder_of_sentence = sentence[len(start_str):]`. This is because we want to return the remainder of the sentence, not the start string. After making this change, I ran the code again and expected the output: "fantastic, I guess programming is fantastic." but got "fantastic,kay". Okay... weird, I put a breakpoint on line 10 and used step into until I got to line 13 where I realized that the return of `replace_substring` was just "kay".

4. Fixing the bug, part 2: Took me awhile staring at line 13, but then I realized that `return sentence[0] + replace_substring(start_str[1:], start_str, replace_str)` should be `return sentence[0] + replace_substring(sentence[1:], start_str, replace_str)` because we want to return the first letter of the sentence, not the first letter of the start string. After making this change, I ran the code again and got the expected output: "fantastic, I guess programming is fantastic."!

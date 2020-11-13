# Week 9 workshop: Code review

This week, you will write your own code to solve the task below. You must complete this and **submit your code before Wednesday 18th November, 10am**, on STACK. Submit your code **as a .py script**.

#### There will be no late submissions allowed!

The workshop task will be focused on practising your **code review** skills with your team, using your own solutions. You will take turns sharing your solution with your group, and collectively review each other's code and give each other constructive feedback. Other model solutions will also be provided to you for further discussion.

Then, after your workshop, you will have 5 days (until the day before your next workshop) to **give a code review to 3 other students**. The marking scheme for peer-assessment will be the same as in Week 6, except that there will be **2 questions** about whether the code is working (one for each function required). Remember to include your tests for this task!

---

### Brief

`pcimedna peh Te blli w!noo srev omla cpee Kyojn edn an ignimmargor p!nohty`

This is a message that is sent to us from future, but to protect it from eavesdropping it is **encrypted**. Luckily, we know the algorithm that was used to **encrypt** this message, which is explained in the four steps below:

1.	Turn all the occurrences of the **word** `I` into lowercase `i`. \
    Example: *I am what I am -> i am what i am*


2.	Re-order the words in the sentence. Swap every odd word with the following even word. For example, swap the first word with the second, the third word with the fourth and so on. If the last word is odd, keep it where it is. \
    Example: *you are in love with me -> are you love in me with*


3.	Replace the first letter of each word with the first letter of the previous word. For the very first word, take the first letter of the last word (since there is no words preceding it). \
    Example: *now you are in love with me -> mow nou yre an iove lith we*
    
    
4.	Reverse the order of the remaining letters in each word (i.e. all the letters excluding the first letter). \
    Example: *mow nou yre an iove lith we -> mwo nuo yer an ievo lhti we*

### The task

In this task, you first write the function `encrypt_it()` which takes an input string, and returns the encrypted version of this string using the algorithm above.

When doing encryption, it is very important to have a **reversible** algorithm. The above algorithm is reversible; write the function `decrypt_it()` which takes an input *encrypted* string, and returns the original unencrypted text. Use this function and find out what the original message from the future is!

#### Testing

To test your algorithm you can use the following sentence:

`This course is fun, but I am tired of programming in Python!`

which turns into 

`iesruo csih T,nu fs i itu bderi tm agnimmargor pf o!nohty Pn`

after encryption.

Note that the punctuations in this algorithm are taken as part of the previous word. For example, `fun,` and `Python!` each count as one word.

For fun, you can decrypt the following encrypted sentences as well:

`mevo l ihti wuo yy mll a i!ylle bo tdetna wtrae hya sy mtu bs iylle b.reggi bhcu`

`tesua cemo Srevereh wssenippa h;o gyeh treveneh wemo s.o gyeh`

You can also start with any sentence, encrypt it and then decrypt the result (or the other way around), and check that you get the same sentence that you started with.

---

## Model solutions

A few model answers will be provided for the task after the submission deadline, to assist you in testing and assessing, and also for further discussion during the workshop.

During the workshop, as in Week 6, you will start by discussing each other's code. Then, if time permits, look at the model answers provided, and figure out how they work. For instance, you could compare them with your own solutions, and profile them to compare their efficiency.

Tests will also be provided to help you test the functions when peer-assessing.

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

level_one = input("Left or right? ").lower()
if level_one == "right":
  print("Game Over!")
  print('''
                                         ,===$$$$$bc.
                                      _,eP",d$$$$$$$$$$$$c.
                                    z$$",e$$$$$$$$$$$$$$$$$"
                                   4$$% PFFF"""""?$$PF""""
                                   ??".,c$$$$$$P??F
                                  .,d$$$$$$$$$$$$. `.
                               ,e'"$$$$$$$$$$$$$$$e ,$e.
                             z$$" .$$$F?$$$$$$$$$$$$bc`?% ..::?e
                           z$$$$ d$$$$ d????$$$$$$$$$$$$P":::::$$e
                         .$$$$$$b<$$$$    ?bc`?$$$$?$$$"u::::::4$$b
                   .cccccc`?$$$$$$$$$$     $$$$.?$FJ$$$d$becc;c$$$$
                   d$$$$$$$$bc"?$$$$$$b. ,d$$$$F $$$$$$$$$$$$$$$$$$
                  d$$$$$$L  `$$bc"?$$$$$c,"???",d`$$$$$$$$$$$$$$P"3
                  $$$$$?$$$ee$$$$$bc"?$$$$$$$$$$Ld$$$$$$$$$$$$$P 4$
                 <$$$$$c `$$""$$$$$$$e,?$$$$$$$$$$$$$$$$$$$$$$".. ?b.
                 `$$$$$$$$$$$u$$$$$$$$P= "$$$$$$$$$$$$$$$$$$b,%%%% $$
                  "$$$$$$$$$$$$$$$F,cd$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F
                   "$$$$$$$$$$$P"z$$$$$$$$$$$$$$$$$$$$$$$$$$$$$PF"
                    `$$$$$$PP".e$$$$$$$$$$$$$$$$$$$$$$$$$$$$"e.
                     "??""  e$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                              "?"""""""" `""?$$$$$$$$$$$$$$$$%
                              .c$$".,ced$C$$bbc,"3?$$$$$$$$$"
                             d$$$d$$$$$$$$$$$$$$$$$$$$$$P"
                            d$$$$$$$$$$$$$$$$$$$$$$e`?$F
                           $$$$$$$$$$$$$$$$$$$$$$$$$$b/
                          d$$$$$$$$$$$$$$$$$$$$$$$$$$$$.
                        ,e$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$b.
                     ,dF .,c$$$$$$$$$$$?$$$$$$$$$$$$$$$$$$.
                   zP??$$$".c$$$$$$$$$$. "$$$$$$$$$$$$$$$$$
                 ,$L.e$$$$$$$$$$$$$$$$$$$$$$ "?$$$$$$$$$$$$F
               ,$$$$$$$$$$$$$$$$$$$$$$$$$$$$b  "$$$$$$$$$$$%
              d$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$be$P$$$$$$$$P
            ,d$$$$P"""$$$$$$$$$$$$$$$$$$$$$$$$$$$$,"?$$$$$"
           z$$??$$,,z$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$u$?$$$$b
          J$$,,$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P$$$$$$$$L$$$$$b
        ,$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$c`?$$$$$`$$$$$$.
  ,e$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$e`?$$ $$$$$$$e
 d$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$b," $$$$$$$$$.
J$$$$$$$$$$$$P??$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P?$,,``..?$P".,c$P,,cc.
3$$$$$$$$$$$F ,c$$$"    z$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$L e$$$$$$$$$$"
`$$$$$$$$$$$$$$$$$$bu$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$b"$$$$$$$$",e
 $$$$$$$$$$P",ed$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$>?$$$$$$$$P"
 `$$$$$$$$",$$"`x3$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"  $P J$$$$$$$"
  `$$$$$$'d$P.$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F  ," z$$$$$P"
    "$$$'$$",$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  ?$$$$$"  e$$P""
      "F,$P,$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$,e$$$$"   ""
       .$P.$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$PF""
       d$    `""?????????$$$$$$$$$$$$$$$$$$$$PFF""
       $"                   ``"""""""""""""`
       $

  ''')

elif level_one == "left":
  level_two = input("Swim or Wait? ").lower()
  if level_two == "swim":
    print("Game Over!")
    print('''
                                         ,===$$$$$bc.
                                      _,eP",d$$$$$$$$$$$$c.
                                    z$$",e$$$$$$$$$$$$$$$$$"
                                   4$$% PFFF"""""?$$PF""""
                                   ??".,c$$$$$$P??F
                                  .,d$$$$$$$$$$$$. `.
                               ,e'"$$$$$$$$$$$$$$$e ,$e.
                             z$$" .$$$F?$$$$$$$$$$$$bc`?% ..::?e
                           z$$$$ d$$$$ d????$$$$$$$$$$$$P":::::$$e
                         .$$$$$$b<$$$$    ?bc`?$$$$?$$$"u::::::4$$b
                   .cccccc`?$$$$$$$$$$     $$$$.?$FJ$$$d$becc;c$$$$
                   d$$$$$$$$bc"?$$$$$$b. ,d$$$$F $$$$$$$$$$$$$$$$$$
                  d$$$$$$L  `$$bc"?$$$$$c,"???",d`$$$$$$$$$$$$$$P"3
                  $$$$$?$$$ee$$$$$bc"?$$$$$$$$$$Ld$$$$$$$$$$$$$P 4$
                 <$$$$$c `$$""$$$$$$$e,?$$$$$$$$$$$$$$$$$$$$$$".. ?b.
                 `$$$$$$$$$$$u$$$$$$$$P= "$$$$$$$$$$$$$$$$$$b,%%%% $$
                  "$$$$$$$$$$$$$$$F,cd$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F
                   "$$$$$$$$$$$P"z$$$$$$$$$$$$$$$$$$$$$$$$$$$$$PF"
                    `$$$$$$PP".e$$$$$$$$$$$$$$$$$$$$$$$$$$$$"e.
                     "??""  e$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                              "?"""""""" `""?$$$$$$$$$$$$$$$$%
                              .c$$".,ced$C$$bbc,"3?$$$$$$$$$"
                             d$$$d$$$$$$$$$$$$$$$$$$$$$$P"
                            d$$$$$$$$$$$$$$$$$$$$$$e`?$F
                           $$$$$$$$$$$$$$$$$$$$$$$$$$b/
                          d$$$$$$$$$$$$$$$$$$$$$$$$$$$$.
                        ,e$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$b.
                     ,dF .,c$$$$$$$$$$$?$$$$$$$$$$$$$$$$$$.
                   zP??$$$".c$$$$$$$$$$. "$$$$$$$$$$$$$$$$$
                 ,$L.e$$$$$$$$$$$$$$$$$$$$$$ "?$$$$$$$$$$$$F
               ,$$$$$$$$$$$$$$$$$$$$$$$$$$$$b  "$$$$$$$$$$$%
              d$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$be$P$$$$$$$$P
            ,d$$$$P"""$$$$$$$$$$$$$$$$$$$$$$$$$$$$,"?$$$$$"
           z$$??$$,,z$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$u$?$$$$b
          J$$,,$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P$$$$$$$$L$$$$$b
        ,$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$c`?$$$$$`$$$$$$.
  ,e$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$e`?$$ $$$$$$$e
 d$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$b," $$$$$$$$$.
J$$$$$$$$$$$$P??$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P?$,,``..?$P".,c$P,,cc.
3$$$$$$$$$$$F ,c$$$"    z$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$L e$$$$$$$$$$"
`$$$$$$$$$$$$$$$$$$bu$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$b"$$$$$$$$",e
 $$$$$$$$$$P",ed$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$>?$$$$$$$$P"
 `$$$$$$$$",$$"`x3$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"  $P J$$$$$$$"
  `$$$$$$'d$P.$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F  ," z$$$$$P"
    "$$$'$$",$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  ?$$$$$"  e$$P""
      "F,$P,$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$,e$$$$"   ""
       .$P.$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$PF""
       d$    `""?????????$$$$$$$$$$$$$$$$$$$$PFF""
       $"                   ``"""""""""""""`
       $
    ''')

  elif level_two == "wait":
    door = input("Which door? Blue, Yellow or Red? ").lower()
    if door == "blue" or door == "red":
      print("Game Over!")
      print('''
                                         ,===$$$$$bc.
                                      _,eP",d$$$$$$$$$$$$c.
                                    z$$",e$$$$$$$$$$$$$$$$$"
                                   4$$% PFFF"""""?$$PF""""
                                   ??".,c$$$$$$P??F
                                  .,d$$$$$$$$$$$$. `.
                               ,e'"$$$$$$$$$$$$$$$e ,$e.
                             z$$" .$$$F?$$$$$$$$$$$$bc`?% ..::?e
                           z$$$$ d$$$$ d????$$$$$$$$$$$$P":::::$$e
                         .$$$$$$b<$$$$    ?bc`?$$$$?$$$"u::::::4$$b
                   .cccccc`?$$$$$$$$$$     $$$$.?$FJ$$$d$becc;c$$$$
                   d$$$$$$$$bc"?$$$$$$b. ,d$$$$F $$$$$$$$$$$$$$$$$$
                  d$$$$$$L  `$$bc"?$$$$$c,"???",d`$$$$$$$$$$$$$$P"3
                  $$$$$?$$$ee$$$$$bc"?$$$$$$$$$$Ld$$$$$$$$$$$$$P 4$
                 <$$$$$c `$$""$$$$$$$e,?$$$$$$$$$$$$$$$$$$$$$$".. ?b.
                 `$$$$$$$$$$$u$$$$$$$$P= "$$$$$$$$$$$$$$$$$$b,%%%% $$
                  "$$$$$$$$$$$$$$$F,cd$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F
                   "$$$$$$$$$$$P"z$$$$$$$$$$$$$$$$$$$$$$$$$$$$$PF"
                    `$$$$$$PP".e$$$$$$$$$$$$$$$$$$$$$$$$$$$$"e.
                     "??""  e$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                              "?"""""""" `""?$$$$$$$$$$$$$$$$%
                              .c$$".,ced$C$$bbc,"3?$$$$$$$$$"
                             d$$$d$$$$$$$$$$$$$$$$$$$$$$P"
                            d$$$$$$$$$$$$$$$$$$$$$$e`?$F
                           $$$$$$$$$$$$$$$$$$$$$$$$$$b/
                          d$$$$$$$$$$$$$$$$$$$$$$$$$$$$.
                        ,e$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$b.
                     ,dF .,c$$$$$$$$$$$?$$$$$$$$$$$$$$$$$$.
                   zP??$$$".c$$$$$$$$$$. "$$$$$$$$$$$$$$$$$
                 ,$L.e$$$$$$$$$$$$$$$$$$$$$$ "?$$$$$$$$$$$$F
               ,$$$$$$$$$$$$$$$$$$$$$$$$$$$$b  "$$$$$$$$$$$%
              d$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$be$P$$$$$$$$P
            ,d$$$$P"""$$$$$$$$$$$$$$$$$$$$$$$$$$$$,"?$$$$$"
           z$$??$$,,z$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$u$?$$$$b
          J$$,,$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P$$$$$$$$L$$$$$b
        ,$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$c`?$$$$$`$$$$$$.
  ,e$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$e`?$$ $$$$$$$e
 d$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$b," $$$$$$$$$.
J$$$$$$$$$$$$P??$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P?$,,``..?$P".,c$P,,cc.
3$$$$$$$$$$$F ,c$$$"    z$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$L e$$$$$$$$$$"
`$$$$$$$$$$$$$$$$$$bu$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$b"$$$$$$$$",e
 $$$$$$$$$$P",ed$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$>?$$$$$$$$P"
 `$$$$$$$$",$$"`x3$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"  $P J$$$$$$$"
  `$$$$$$'d$P.$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F  ," z$$$$$P"
    "$$$'$$",$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  ?$$$$$"  e$$P""
      "F,$P,$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$,e$$$$"   ""
       .$P.$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$PF""
       d$    `""?????????$$$$$$$$$$$$$$$$$$$$PFF""
       $"                   ``"""""""""""""`
       $
      ''')

    elif door == "yellow":
      print("You Win! The treasure is yours!")
      print('''
      *******************************************************************************
                |                   |                  |                     |
       _________|________________.=""_;=.______________|_____________________|_______
      |                   |  ,-"_,=""     `"=.|                  |
      |___________________|__"=._o`"-._        `"=.______________|___________________
                |                `"=._o`"=._      _`"=._                     |
       _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
      |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
      |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
       _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
      |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
      |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
      ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
      /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
      ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
      /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
      ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
      /______/______/______/______/______/______/______/______/______/______/_____ /
      *******************************************************************************
      ''')


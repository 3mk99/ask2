print("""""


               AAA
              A:::A
             A:::::A
            A:::::::A
           A:::::::::A              mmmmmmm    mmmmmmm      mmmmmmm    mmmmmmm     aaaaaaaaaaaaa  rrrrr   rrrrrrrrr
          A:::::A:::::A           mm:::::::m  m:::::::mm  mm:::::::m  m:::::::mm   a::::::::::::a r::::rrr:::::::::r
         A:::::A A:::::A         m::::::::::mm::::::::::mm::::::::::mm::::::::::m  aaaaaaaaa:::::ar:::::::::::::::::r
        A:::::A   A:::::A        m::::::::::::::::::::::mm::::::::::::::::::::::m           a::::arr::::::rrrrr::::::r
       A:::::A     A:::::A       m:::::mmm::::::mmm:::::mm:::::mmm::::::mmm:::::m    aaaaaaa:::::a r:::::r     r:::::r
      A:::::AAAAAAAAA:::::A      m::::m   m::::m   m::::mm::::m   m::::m   m::::m  aa::::::::::::a r:::::r     rrrrrrr
     A:::::::::::::::::::::A     m::::m   m::::m   m::::mm::::m   m::::m   m::::m a::::aaaa::::::a r:::::r
    A:::::AAAAAAAAAAAAA:::::A    m::::m   m::::m   m::::mm::::m   m::::m   m::::ma::::a    a:::::a r:::::r
   A:::::A             A:::::A   m::::m   m::::m   m::::mm::::m   m::::m   m::::ma::::a    a:::::a r:::::r
  A:::::A               A:::::A  m::::m   m::::m   m::::mm::::m   m::::m   m::::ma:::::aaaa::::::a r:::::r
 A:::::A                 A:::::A m::::m   m::::m   m::::mm::::m   m::::m   m::::m a::::::::::aa:::ar:::::r
AAAAAAA                   AAAAAAAmmmmmm   mmmmmm   mmmmmmmmmmmm   mmmmmm   mmmmmm  aaaaaaaaaa  aaaarrrrrrr







""")

Name = input("What is your name?: ")

try:
    Name_confirmation = input("Are you sure your name is " + Name + "? : ")

    if Name_confirmation.lower() == "yes":
        print("Ok, nice name")
    elif Name_confirmation.lower() == " yes":


        print("Ok, nice name")

    elif Name_confirmation.lower() == " yes ":

        print("Ok, nice name")
    elif Name_confirmation.lower() == "yes ":

        print("Ok, nice name")
    else:
        print("Go to hell")

except ValueError:
    print("Invalid input. Please enter a valid response.")

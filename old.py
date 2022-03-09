print('''
__      __ _____________________       _____________________________   ____ ___ __________ ___________ 
/  \    /  \\_   _____/\______   \     /   _____/\_   _____/\_   ___ \ |    |   \\______   \\_   _____/ 
\   \/\/   / |    __)_  |    |  _/     \_____  \  |    __)_ /    \  \/ |    |   / |       _/ |    __)_  
 \        /  |        \ |    |   \     /        \ |        \\     \____|    |  /  |    |   \ |        \ 
  \__/\  /  /_______  / |______  /    /_______  //_______  / \______  /|______/   |____|_  //_______  / 
       \/           \/         \/             \/         \/         \/                   \/         \/  
                                                                                                        ''')
with open("old.txt","r")as f:
                            lines=f.readlines()
                            with open("output.txt",'w+') as nf:
                                                              for line in lines:
                                                                               line = line.split(" ")
                                                                               print("IP\t Date time \t Time zone \t Request type \t Path \t HTTP protocol \t Status code \t Packet size \t User Info")
                                                                               nf.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(line[0].replace('"',' '),line[3].replace('"',' '),line[4].replace('"',' '),line[5].replace('"',' '),line[6].replace('"',' '),line[7].replace('"',' '),line[8].replace('"',' '),line[9].replace('"',' '),line[11].replace('"',' ')))
                                      # print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(line[0].replace('"',' '),line[3].replace('"',' '),line[4].replace('"',' '),line[5].replace('"',' '),line[6].replace('"',' '),line[7].replace('"',' '),line[8].replace('"',' '),line[9].replace('"',' '),line[11].replace('"',' ')))

                                                                                                                  
                                                                                             
                                           

w nlp nie korzystamy z ROSa (póki co),

chatbot_united to połączenie małych sieci (ofertowej, smalltalk) w jedną większą

odpalanie:

chatbot_united/chatbot_api.py -> dwa tryby tekstowy i głosowo-tekstowy (ustawiany fląga voice=True/False)

przy voice=True ważne jest dokładne sprawdzenie poprzypinanych urządzeń audio (input/output)

**WAŻNE**

**do prawidłowego działania potrzebny jest tensorflow 2+. zaleca się NIE instalować go za pomocą pip**



voice to wartośc boolowska, tekstowy dla False i głosowo-tekstowy dla True
buisness_hit to wartośc boolowska, uruchamia nakierowania na biznes dla True

najważniejsze metody klasy Chatbot:

chat(voice) -> pętla rozmowy (przestarzałe)
ask(voice) -> pojedyncze pytanie do robota

najważniejsze metody klasy Chatflow:

flow(voice, buisness_hint) -> aktualna pętla rozmowy (w budowie, czeka na połączenie z modułem wizyjnym)



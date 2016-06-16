def decode(message):
    decoder = []
    buenos = []
    n = 0
    for char in message:
        decoder.append(char)
    for clave in decoder:
        if clave.isdigit():
            buenos.append(decoder[n+int(clave)+1])
        n += 1
    print("".join(buenos))

decode("0h2abe1zy")
decode("b1xaervthum3mmodr1fr0itw5dcexyavd0nwrudutt2era")
decode("hrs2irva0arts4woeil2onertrs0nie2oit3nweindne2oenbrapapap")

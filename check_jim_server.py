from mcstatus import MinecraftServer
from flask import Flask, jsonify,render_template
import os



app = Flask("__name__")

@app.route('/')
def players():
    server_info = "52.207.3.215:25565"
    data = {}

    data["server"] = server_info
    # If you know the host and port, you may skip this and use MinecraftServer("example.org", 1234)
    try:
        server = MinecraftServer.lookup(server_info)
        status = server.status()

    except Exception as e:
        print e
        data["error"] = str(e)
        return jsonify(data)


    # 'status' is supported by all Minecraft servers that are version 1.7 or higher.
    print "status",server.status()
    data["status.latency"] = status.latency
    data["currently_online"] = status.players.online

    print("The server has {0} players and replied in {1} ms".format(status.players.online, status.latency))
    if status.players.online > 0:
        print status.players.stu[u'sample']
        data["players"] = []
        for p in status.players.stu[u'sample']:
            data["players"].append(p[u'name'])
        print "data",data
        # 'ping' is supported by all Minecraft servers that are version 1.7 or higher.
        # It is included in a 'status' call, but is exposed separate if you do not require the additional info.
    
    latency = server.ping()
    data["server.latency"] = str(latency)
    print("The server replied in {0} ms".format(latency))

    # 'query' has to be enabled in a servers' server.properties file.
    # It may give more information than a ping, such as a full player list or mod information.
    # query = server.query()
    # print("The server has the following players online: {0}".format(", ".join(query.players.names)))

    return jsonify(data)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))

    if port == 5001:
        app.debug = True

    app.run(host='0.0.0.0', port=port)
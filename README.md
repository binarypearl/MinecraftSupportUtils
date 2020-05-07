# MinecraftSupportUtils
Support utiles for running a Minecraft server

Tool 1: fah_pause_toggle - Query Minecraft port for user count.  If 0, unpause F@H.  If user is 1 or more, pause F@H.

Usage:  ./fah_pause_toggle/pause_unpause_fah.py -s 192.168.1.223 -p 25565

Replace your IP and port accordingly.


Tool 2:  Still in developement, server_jar_swap, an auto-snapshot updater.  When MC releases a new snapshot, the server has to be updated as well.  Found a way to query MC servers to see new version (it's not trivial).  Plan to eventually have it where a server can auto-update itself once a new snapshot is released.

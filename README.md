# nifi-play
Play area for setting up nifi

The demo can be configured using
```
# in services
docker-compose build
```
followed by
```
# in services
docker-compose up
```
There may be some perms issues on the mount folders created by "docker-compose up"; if so, bring the services down, upgrade the perms on the created folders, and restart the services.

Access to the nifi and nifi-registry APIs can be verified by
```
curl http://localhost:18080/nifi-registry-api/access
curl http://localhost:8091/nifi-api/system-diagnostics
```
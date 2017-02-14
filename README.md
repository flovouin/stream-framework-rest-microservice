# Description

This repository shows how to use [Stream-Framework](https://github.com/tschellenbach/Stream-Framework) to create a simple API to manage feeds. Users follow other users, they post activities, and their respective feeds get updated. `Stream-Framework` uses `Cassandra` for storage and `Celery` to distribute computing. This example provides a `Celery` worker to give a rough idea of how this could work in production. `Django` and the `Django REST Framework` are used to handle HTTP requests.

JWT authentication is handled, although any authenticated user can add follow relationships and activities, which is obviously not safe. In a microservice architecture, these events would be received from other services. A mocked follow service is provided simply to make the example runnable. JWT are only really used to get the current user for the `/feeds/aggregated` end point. Also, Django user management is not used: we assume that tokens are issued by a separate authentication service.

Oh yeah, obviously, this is not production ready.

# Run the example

Start the containers with `docker-compose`:

```bash
docker-compose up
```

Set up Cassandra by creating the relevant keyspace and tables:

```bash
docker-compose run -e CQLENG_ALLOW_SCHEMA_MANAGEMENT=1 activity python db_setup.py
```

Restart the API:

```bash
docker-compose restart activity
```

Test that everything works by issuing simple commands:

```bash
# Token that can be generated from http://jwt.io using the private and public keys in the etc folder.
JWT="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c3JfMDIifQ.XSaKEn61nL8hn9c-4rc58lsuK6upOfTAk7qstQSi2nU6liR4vM2v5IMHFGOZv6noQ9yCX9qANa3GFoE63HLpvTSimUL4B1Jxo-AmRuN_6EvPXCICjo9FobPJ_19UpADcmltf8wi1no5V48fz5g9pG0pp9NTyFwOjpcty9i1-Ah9juhlxjVPJamWClHcnebHvAxQeabrEnPFNKgLYeI-a0EqyNYPcCYyciPBU1lWHlE9Qsxf7_8wr9SL6FBTERMMDvdFAd7n5qVeMd_kXoXIgL3qZNeA9lLIfSfOoqszG4qtcczCbsEfxl_7BSNexc-Fl2_1a6lHxGnxiLcB8nNcWlA"
# Make usr_02 follow usr_01.
curl -X POST -H "Content-type: application/json" -H "authorization: JWT $JWT" -d '{ "follower": "usr_02", "following": "usr_01" }' localhost:1234/follow
# Adds a new activity for usr_01.
curl -X POST -H "Content-type: application/json" -H "authorization: JWT $JWT" -d '{ "actor": "usr_01", "object": "obj_50", "target": "usr_73" }' localhost:1234/activities
# Check that the aggregated feed (timeline) of usr_02 now contains the activity of usr_01.
curl -H "authorization: JWT $JWT" localhost:1234/feeds/aggregated
```

# Implementation

This example uses a [forked version](https://github.com/flovouin/Stream-Framework) of Stream-Framework, only to allow for non-integer IDs for users and objects with the Cassandra backend.

The `follow` service provides a very basic logic to keep the follow graph in memory. This is not meant for production.

The `/feed/aggregated` endpoint does not implement pagination. This would be a nice improvement to this example.

The `/follow` endpoint could also notify Stream-Framework, to add past "followee" activities to the feed of the follower.

As mentioned previously, authentication only checks for a valid JWT using the public key in `settings.py`. This is not sufficient to protect the API. It just shows how to add JWT authorization without relying on Django user model.

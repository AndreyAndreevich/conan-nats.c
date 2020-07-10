#include <nats.h>

static void
onMsg(natsConnection *nc, natsSubscription *sub, natsMsg *msg, void *closure)
{
    printf("Received msg: %s - %.*s\n",
           natsMsg_GetSubject(msg),
           natsMsg_GetDataLength(msg),
           natsMsg_GetData(msg));

    // Need to destroy the message!
    natsMsg_Destroy(msg);

    // Notify the main thread that we are done.
    *(bool *)(closure) = true;
}

int main(int argc, char **argv)
{
    natsConnection      *conn = NULL;
    natsSubscription    *sub  = NULL;
    natsStatus          s;
    volatile bool       done  = false;

    // Creates a connection to the default NATS URL
    s = natsConnection_ConnectTo(&conn, NATS_DEFAULT_URL);
    natsConnection_Destroy(conn);

    return 0;
}
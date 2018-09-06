
import time
import grpc
import logging
from concurrent import futures
from proto.example import example_pb2, example_pb2_grpc
from proto.health import health_pb2, health_pb2_grpc

logging.basicConfig(format='%(asctime)s:%(message)s', level=logging.DEBUG)

class Example(example_pb2_grpc.ExampleServicer):
    def Call(self, request, context):
        return example_pb2.Response(msg="Hello, %s!" % request.name)

class Health(health_pb2_grpc.HealthServicer):
    def Check(self, request, context):
        return health_pb2.HealthCheckResponse(status=1)

def main():
    port = 50001
    # 创建服务
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    example_pb2_grpc.add_ExampleServicer_to_server(Example(), server)
    health_pb2_grpc.add_HealthServicer_to_server(Health(), server)
    address = "[::]:%d" % port
    server.add_insecure_port(address)
    server.start()
    logging.info("Listening on %s" % address)
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    main()
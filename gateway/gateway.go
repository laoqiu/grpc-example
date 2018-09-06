package main

import (
	"flag"
	"log"
	"net/http"
	"time"

	"github.com/grpc-ecosystem/grpc-gateway/runtime"
	"golang.org/x/net/context"
	"google.golang.org/grpc"

	example "laoqiu.com/grpc-example/proto/example"
	health "laoqiu.com/grpc-example/proto/health"
)

var (
	endpoint = flag.String("endpoint", "localhost:50001", "endpoint of Server")
)

func startGatewayServer() error {
	ctx := context.Background()
	ctx, cancel := context.WithCancel(ctx)
	defer cancel()

	mux := runtime.NewServeMux()
	opts := []grpc.DialOption{grpc.WithInsecure()}

	// 注册handler
	if err := example.RegisterExampleHandlerFromEndpoint(ctx, mux, *endpoint, opts); err != nil {
		return err
	}

	return http.ListenAndServe(":8080", mux)
}

func startCheckHealth() error {
	conn, err := grpc.Dial("127.0.0.1:50001", grpc.WithInsecure())
	if err != nil {
		return err
	}
	defer conn.Close()

	client := health.NewHealthClient(conn)

	for {
		req := new(health.HealthCheckRequest)
		r, err := client.Check(context.Background(), req)
		if err != nil {
			//switch grpc.Code(err) {
			//case
			//	codes.Aborted,
			//	codes.DataLoss,
			//	codes.DeadlineExceeded,
			//	codes.Internal,
			//	codes.Unavailable:
			//default:
			//	return err
			//}
			return err
		}

		log.Println("health check status: ", r.Status)

		<-time.After(time.Second * 3)
	}
}

func main() {
	errors := make(chan error)
	go func() {
		errors <- startGatewayServer()
	}()

	go func() {
		errors <- startCheckHealth()
	}()

	for err := range errors {
		log.Fatal(err)
	}
}

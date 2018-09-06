package main

import (
	"log"
	"net"
	"sync"

	"golang.org/x/net/context"
	"google.golang.org/grpc"
	"google.golang.org/grpc/reflection"
	example "laoqiu.com/grpc-example/proto/example"
	health "laoqiu.com/grpc-example/proto/health"
)

const (
	port = ":50001"
)

type Example struct{}

func (s *Example) Call(ctx context.Context, in *example.Request) (*example.Response, error) {
	return &example.Response{Msg: "Hello " + in.Name}, nil
}

type Health struct {
	mu sync.Mutex
}

func (s *Health) Check(ctx context.Context, req *health.HealthCheckRequest) (*health.HealthCheckResponse, error) {
	s.mu.Lock()
	defer s.mu.Unlock()
	result := &health.HealthCheckResponse{
		Status: health.HealthCheckResponse_SERVING,
	}
	return result, nil
}

func startRPCServer() error {
	lis, err := net.Listen("tcp", port)
	if err != nil {
		return err
	}
	s := grpc.NewServer()
	example.RegisterExampleServer(s, &Example{})
	health.RegisterHealthServer(s, &Health{})
	// Register reflection service on gRPC server.
	reflection.Register(s)
	if err := s.Serve(lis); err != nil {
		return err
	}
	return nil
}

func main() {
	if err := startRPCServer(); err != nil {
		log.Fatal(err)
	}
}

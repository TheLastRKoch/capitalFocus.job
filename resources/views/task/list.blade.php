@extends('layouts.app')

@section('content')
    <section id="ItemList">
        <div class="container">
            <div class="card">
                <div class="card-body">
                    <div class="card-title">
                        <h5>Tasks</h5>
                    </div>
                    <div class="row">
                        <div class="col-xl-12 mx-auto">
                            @if(count($Tasks))
                                <table class="table">
                                <thead>
                                <tr>
                                    <th scope="col">Name</th>
                                    <th scope="col">State</th>
                                    <th scope="col">Difficulty</th>
                                    <th scope="col">Priority</th>
                                    <th scope="col">Start</th>
                                    <th scope="col">Time postponed</th>
                                    <th scope="col">End date</th>
                                    <th scope="col">Duration time</th>
                                    <th scope="col"></th>
                                </tr>
                                </thead>
                                <tbody>
                                @foreach($Tasks as $Task)
                                    <tr>
                                        <td scope="col">
                                            <a href="{{route('task.update',['id'=>$Task->id])}}">{{$Task->Name}}</a>
                                        </td>
                                        <td scope="col">{{$Task->State}}</td>
                                        <td scope="col">{{$Task->Difficulty}}</td>
                                        <td scope="col">{{$Task->Priority}}</td>
                                        <td scope="col">{{$Task->StartDate}}</td>
                                        <td scope="col">{{$Task->TimePostponed}}</td>
                                        <td scope="col">{{$Task->EndDate}}</td>
                                        <td scope="col">{{$Task->PeriodTime}}</td>
                                        <td scope="col">
                                            <a href="{{route('task.delete',['id'=>$Task->id])}}">X</a>
                                        </td>
                                    </tr>
                                @endforeach
                                </tbody>
                            </table>
                            @else
                                <p>No hay elementos que mostrar</p>
                            @endif
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section><!--Task table-->

@endsection

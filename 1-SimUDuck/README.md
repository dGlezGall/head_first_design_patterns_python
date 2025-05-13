# SimUDuck (Strategy Pattern)

Simple implementation of the Strategy Pattern following the first chapter's example: the "SimUDuck" app

## Run the example
Supposing you have cloned the repository and are in the root folder, run:
```bash
cd ./1-SimUDuck
py -3.12 ./main.py
```

## Project Structure

```
1-SimUDuck/
├── strategies/
|   ├── fly.py        # Fly interface
|   ├── flights/      # Flying strategies implementations
|   |
|   ├── quack.py      # Quack interface
|   └── quacks/       # Quacking strategies implementations
|
├── ducks/            # Duck interface and it's implementations
└── main.py
```

## Insights
This example demonstrates several key design principles:

1. **Dynamic Behavior Changes**: Run the example, check [./main.py](./main.py) and see how the `RubberDuck` changes its flying behavior at runtime.

2. **Strategy Pattern**: The example implements the Strategy Pattern, which enables selecting algorithms at runtime. Here, flying and quacking behaviors can be changed dynamically.

3. **Programming to Interfaces**: The code demonstrates the principle of programming to interfaces, not implementations:
   - [`Duck`](./ducks/duck.py) is an abstract base class (interface) that concrete ducks implement
   - [`FlyStrategy`](./strategies/fly.py) and [`QuackStrategy`](./strategies/quack.py) are interfaces for behaviors
   - Concrete strategies (like [`FlyWithWings`](./strategies/flights/fly_with_wings.py), [`NormalQuack`](./strategies/quacks/normal_quack.py)) implement these interfaces

4. **Composition over Inheritance**: Instead of using inheritance to define duck behaviors, we use composition by injecting behavior objects. This makes the system more flexible and behaviors interchangeable.

## Class Diagram

```
┌──────────────────┐               ┌───────────────┐
│     <<ABC>>      │               │    <<ABC>>    │
│     Duck         │               │     Fly       │
├──────────────────┤     (has-a)   ├───────────────┤
│ +fly_behavior    │◆────────────>│ +fly()         │
│ +quack_behavior  │◆─────────┐   └───────┬────────┘
├──────────────────┤          │            │
│ +swim()          │          │      ┌─────┴───────┐
│ +display()       │          │      │             │
│ +perform_fly()   │          │    ┌─┴──────┐ ┌────┴─────┐
│ +perform_quack() │          │    │FlyNoWay│ │FlyWith   │
└───────┬──────────┘          │    │        │ │Wings     │
        │  (is-a)             │    └────────┘ └──────────┘
    ┌───┴───────┐             │
    │           │             │   ┌───────────────┐
┌───┴────┐  ┌───┴───┐         │   │   <<ABC>>     │
│Mallard │  │Rubber │         │   │    Quack      │
│Duck    │  │Duck   │         └──>├───────────────┤
└────────┘  └───────┘             │ +quack()      │
                                  └───────┬───────┘
                                          │
                                 ┌────────┴────────┐
                                 │                 │
                             ┌───┴────┐       ┌────┴─────┐
                             │Normal  │       │Squeak    │
                             │Quack   │       │Quack     │
                             └────────┘       └──────────┘
```

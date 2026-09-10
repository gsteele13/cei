(lecture1)=
# Review of Voltages, Currents, and Kirchoffs Laws

> In this lecture, we will jump back into electrical circuits! We will start by reviewing familiar concepts, such as voltage, currents, and Kirchoff's laws. While we are doing this, we take a closer look at the wires, nodes, and brances we draw in our circuits to get a better understanding of what they mean. We will look at the superposition principle for circuits, as both a conceptual shortcut for solving certain trikier problems, and as a more general concept for the case when we have multiple types of signals in our circuit, such as AC and DC voltages and currents. Finally, although the superposition principle breaks down in general for nonlinear circuits, we will see that it can still be useful in some cases, foreshadowing the "small signal models", a type of perturbation theory for circuits, that we will study later in the course.

<!-- (lo-l1)=
## Learning objectives Lecture 1
And the learning objectives
1. none
2. none
3. none -->

## Basics of Voltage and Current in electrical circuits

### Voltage

 The concept of voltage comes from [electrostatics](https://en.wikipedia.org/wiki/Electrostatics). Electrostatics if founded on [Coulomb's law](https://en.wikipedia.org/wiki/Coulomb%27s_law), which describes the force between two fixed charged particles:

$$
F = \frac{1}{4\pi\epsilon} \frac{q_1 q_2}{r^2}
$$

Two charges of the opposite sign attract, and two charges of the same sign repel. 

In general, one can extend this to the force exerted on a test charge $q_0$ by N charges using a large vector sum:

$$
\mathbf{F} = \frac{q_0}{4\pi \epsilon} \sum_{i=1}^{N} \frac{q_i}{\|\mathbf{r}_0 - \mathbf{r}_i\|^3} (\mathbf{r}_0 - \mathbf{r}_i)
$$

Note that the second part of the expression does not depend on the charge of the test charge, but only on the the position $\mathbf{r}_0$ of the test charge and the charges of all the other particles, leading the the concept of the [Electric Field](https://en.wikipedia.org/wiki/Electric_field): a vector that is property of the space at the position of the test charge due to all the other particles.

In electrostatics, you can write this electric field as the gradient of scalar field, known as the [electrostatic potential](https://en.wikipedia.org/wiki/Electric_potential), which we will denote in this course by the letter $V$: 

$$
\mathbf{E(r)} = - \nabla V(\mathbf{r})
$$

Electrostatic potential is measured in the unit of [Volts](https://en.wikipedia.org/wiki/Volt), hence the choice of the letter $V$ in this course! 

Note that the absolute value of the voltage is arbitrary: I can add a constant (position independent) offset $V_0$ to the definition of $V$ and it will not change the value of any electric fields and therefore not any forces between charges (an example of [gauge invariance](https://en.wikipedia.org/wiki/Volt)). 

While the specific value of the potential does not have a meaning, the *relative* value of the electrostatic potential at two different positions in space *does* have physical meaning: it tells you how much the [potential energy](https://en.wikipedia.org/wiki/Potential_energy) $U$ of the charged particle changes if you moved it from position $\mathbf{r_1}$ to position $\mathbf{r_2}$:

$$
\Delta U = q\left[ V(\mathbf{r_2}) - V(\mathbf{r_1}) \right]
$$

What about voltages in circuits? 

Voltages in circuits tells us the same thing: it tells us how much the potential energy of a charge will change if we let it flow from one position to another in the circuit. 

### Ideal wires

When we draw a circuit, though, things are a bit different than when we consider isolated charges floating around in free space. Electrical circuits consists of metals: as we know from electrostatics, if there is no current flowing in the metal, the electric field inside of it is always zero. 

In our theoretical lectures, we will draw circuit elements connected by wires, and it is very important to understand what these wires mean when we draw them. Specifically, thess are special theoretical "ideal wires. In ideal wires, the voltage *everywhere* in that wire is always the same, instantaneously! In our schematics, the voltage across anything we draw a "wire" is **always** by definition zero.

```python
with schemdraw.Drawing():
    R1 = elm.Resistor().dot()
    R2 = elm.Resistor().down().dot()
    L = elm.Line().left().dot()
    elm.SourceV().up().label('10V').dot()
    elm.VoltageLabelArc().at(R1).label(r'$\DeltaV_1$')
    elm.VoltageLabelArc().at(R2).label(r'$\DeltaV_2$')
    elm.VoltageLabelArc().at(L).label(r'$\Delta$V = 0 Always for (ideal) wires!')
```

What goes into our model of the "ideal wire" that we draw as lines in our schematics? This approximation is valid if:

1. The ideal wire has zero resistance
2. The ideal wire has zero (self) inductance
3. The ideal wire has zero (self) capacitance
   
If these three assumptions hold, then the wires in our schematics *instantaneously* "teleport" voltage from their input node to their output node with zero change in value. It does not matter how long we draw them in our circuit: as short wire and a long wire in our schematics are exactly equivalent!

#### Warning: Ideal wires are different than real life wires!

The instantaneous and perfect propgation of changes of voltage is not the case for *real life* wires you will use in your circuit! Wires in real life have non-zero resistance, non-zero inductance, and non-zero capacitance to ground. 

In practice, compared to the impedance ('resistance to charge flow') of the [lumped elements](https://en.wikipedia.org/wiki/Lumped-element_model) we will draw in our circuit, the resistance of wires is very small, even for very skinny ones like you will use in the lab course. Concretely, the hookup wire used in the lab is typically 22 [AWG](https://en.wikipedia.org/wiki/American_wire_gauge). Using the conductivity of copper, a 15 cm wire then [has a resistance](https://share.gemini.google/uQq6RTxwSn6j) of 0.008 Ohms (8 milliohms). The smallest resistor you have use in your lab experiment box is 10 ohms: compared even to 10 Ohms, it is clear that 0.008 ohms, it is clear that it is a very good approximation that wires in your experiments have zero ohm resistance. 

*Note that the resistance of the 15 cm wire is actually lower that the [typical contact resistance](https://share.gemini.google/Sk6tbpaKRJOF) of 10-20 milliohms associated with the [header pins](https://en.wikipedia.org/wiki/Pin_header) you will use to connect them to the [breadboard](https://en.wikipedia.org/wiki/Breadboard) you will use in the lab.*

In addition to resistance, all real-life wires will also have an [inductance](https://en.wikipedia.org/wiki/Inductance) which will resist the *change* of current in the wire, arising from the energy that needs to build up in the magnetic fields around the wire when the current flows. How big is the inductance of the wires in your setup? This is, in general, a complicated question to answer since it depends on how close that wire is to the flow of the current back to the source. One way to estimate this is to assume that the current flowing back is infinitelly far away: this will give you an *upper* bound on the inductance. The magnetic fields around an infinite one-dimensional wire is a problem you have certainly solved (or could easily solve) from the [magnetostatics](https://en.wikipedia.org/wiki/Magnetostatics) you learned in your electromagnetism course. It will logarithmically depend on the radius of the wire, but a typical practical value to keep in mind is about [1 nH per mm](https://share.google/aimode/gbfbW8ACAGBTr42xF). For DC currents, or sufficiently low frequencies, you will not need to worry about this: a 1 nH inductor presents an impedance of only $10^{-9}$ ohms for a 1 Hz AC signal. 

Wires also have capacitance: unlike inductance or resistance, capacitance of a wire is not from one end to the other, but from the metal of the wire to ground or other parts of the circuit. How big are these capacitances? The rule of thumb is that the order of magnitude of the total capacitance of a wire to "other stuff" is around 1 pF per centimeter, based on the self-capacitance of an isolated sphere to infinity. This is also a pretty small number: if you consider a 1 MOhm resistor feeding a 1 cm wire, this will produce an RC time of 1 microsecond (small, but actually measureable).

Note that you *can* include these effects of "non-ideal" wires in your modelling of the circuit by adding lumped (or [distributed](https://en.wikipedia.org/wiki/Distributed-element_model)) elements to account for the behaviour of the wire to your circuit model, and we will do that later in the course! But for now, working at low enough frequencies and with low enough resistance wires, our "ideal wires" are good approximations of the actual wires in the circuits you will make. And even when we takle how do deal with "real wires" theoretically, we will break them down into discrete lumped elements that we will always draw connected by "ideal circuit diagram wires". 

### Voltages in ciruits

Once we have accepted ideal wires as little tunnels that instantaneously equilabrate voltages from one node of the circuit to the other, then life in theoretical circuit analysis becomes realatively simple: we do not need to solve the 3-dimensional partial differential equations that come from Coulomb's law from electrostatics, or Ampere's law from magnetostatics. All of the complexity of your electromagnetism courses is mapped into the voltage dropped across the lumped elements we draw in our circuit.

While this seems like a drastic approximation, it can be highly accurate, and if you are really committed, you can actually rebuild all of 3-dimensional electromagntism by meashing 3-dimensional space into a network of nodes that you connect with (mutual) inductances and capacitances, which is what you actually do when you [solve electromagnetic problems with finite element methods](https://en.wikipedia.org/wiki/Computational_electromagnetics).

### Ohms law and sign conventions

One of the circuit elements you have certainly studied in the past is a [resistor](https://en.wikipedia.org/wiki/Resistor). A resistor is a circuit element which produces a current proportional to the voltage drop across it:

$$
\Delta V = IR
$$

For our resistor, and also in general for all of the components we will study, the voltage drops between the two nodes of the component and the current flows from one node to the other. Note it is important to get the convensions of signs right when you draw this in a circuit: in the equation above, the voltage drop follows the same direction as the current flow:

```python
with schemdraw.Drawing():
    R = elm.Resistor().down().dot().idot()
    elm.VoltageLabelArc().at(R).label(r'$\Delta$V')
    elm.CurrentLabelInline(direction='in').at(R).label('I')
```

For the choice of convention that the current is flowing downwards, and if we choose to define the bottom of the resistor as ground, then you will get a voltage $V = IR$ at the upper node:

```python
with schemdraw.Drawing():
    elm.Dot().label("$V$", loc="right")
    R = elm.Resistor().down().dot()
    elm.Ground()
    elm.CurrentLabelInline(direction='in').at(R).label('I')
```

This then shows the convention choice associated with the usual formulation of Ohms law that relates current and voltage:

$$
V = IR
$$


Note that in the convention above, with the direction of the current as shown such that $I$ is a positive number, then $V$ is also a positive number following Ohm's law.

When we study inductors and capacitors, we will encounter similar linear relations between voltages and currents and their integrals / derivatives, and we will follow the same sign convention introduced here. 


## Kirchoff's laws

When connecting elements together in circuits, the relation of the voltages at the different nodes and the currents in different branches of the circuit are given by [Kirchoff's Laws](https://en.wikipedia.org/wiki/Kirchhoff%27s_circuit_laws).

### Kirchoff's current law

The first of Kirchoff's laws is related to the conservation of charge. Since the ideal wires we draw in our circuit diagrams have no capacity to hold charge (capacitance), the currents flowing in and out of any node in the circuit must sum up to zero:


```python
import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    W1 = elm.Line().dot()
    with d.hold():  # Save this drawing position/direction for later
        W2 = elm.Line().down()  # Go off in another direction temporarily
    W3 = elm.Line()

    # Position arrows at the middle of each wire segment using ofst=0.5
    elm.CurrentLabelInline(direction='in', start=False, ofst=0).at(W1).label(r'$I_1$').reverse()
    elm.CurrentLabelInline(direction='in', ofst=0).at(W2).label(r'$I_2$')
    elm.CurrentLabelInline(direction='in', ofst=0).at(W3).label(r'$I_3$')
```

In the schematic here, the three wires are connected at a point in the circuit shown by a dot: this dot is referred to as **[nodes](https://en.wikipedia.org/wiki/Node_(circuits))** of the circuit. 

*(We will sometimes explicity draw dots, sometimes not. Dots in CAD drawings of circuits are also often used to explicity indicate that crossing wires are connected. There are [varying conventions](https://upload.wikimedia.org/wikipedia/commons/3/36/Wire_Crossover_Symbols_for_Circuit_Diagrams.png) on this, and you will encounter both, you should try to use some logical thinking to figure out which one is relevant, and ask if you are not sure. In any case, even if there is not a dot, any set of connected wires is always equivalent to a node.)* 

The voltage on each node is also equal to the voltage and on all wires connected to, in that sense, from a voltage point of view, all wires connected to the node are also consider as the the same "node" of the circuit (see this the [image](https://upload.wikimedia.org/wikipedia/commons/9/95/Nodes2.svg) on the [wikipedia page](https://en.wikipedia.org/wiki/Node_(circuits)) for example). 

The wires connected to the node are referred to as [branches](https://en.wikipedia.org/wiki/Nodal_analysis). As you can see in the figure, although the three wires have the same voltage, they can have *different* currents. 

This brings us to Kirchoff's current law: the sum of the currents from all branches connected to a node must be zero:

$$
\sum_{i=1}^n I_i = 0
$$



Note that we have chosen a particular convention in this equation for the sign of the currents: currents flowing into the node have the opposite sign of currents flowing out of the node. The conventional choice for signs is:

* Currents flowing into the node are consider positive
* Currents flowing out of the node are considered negative

In the example above, with $I_1$, $I_2$, and $I_3$ all chosen to be positive numbers, this leads to:

$$
I_1 - I_2 - I_3 = 0
$$

Or equivalently, the total current flowing out is equal to the total current flowing in:

$$
I_1 = I_2 + I_3
$$

```python

```

```python

```

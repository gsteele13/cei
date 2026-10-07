---
jupyter:
  jupytext:
    default_lexer: ipython3
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.19.4
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

(lecture1)=
# Review of Voltages, Currents, and Kirchoffs Laws

> In this lecture, we will jump back into electrical circuits! We will start by reviewing familiar concepts, such as voltage, currents, and Kirchoff's laws. While we are doing this, we take a closer look at the wires, nodes, and brances we draw in our circuits to get a better understanding of what they mean. We will look at the mathematical formulation of Kirchoff's laws and see how to translate the circuits into equations using them. We will look at the superposition principle for circuits, as both a conceptual shortcut for solving certain trikier problems, and as a more general concept for the case when we have multiple types of signals in our circuit, such as AC and DC voltages and currents and small signal analysis.

<!-- (lo-l1)=
## Learning objectives Lecture 1
And the learning objectives
1. none
2. none
3. none -->

* Basics of Votlage and Current in electrical circuits
  * Voltage
  * Ideal wires
  * Votlage in circuits
  * Ohm's Law
* Kirchoff's Laws
  * Kirchoff's Voltage Law
  * Kirchoff's Current Law
  * Series and Parallel Combinations of Resistors
  * Example of using Kirchoff's laws
* The Superposition Principle
  * Example of solving a circuit using superposition


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

In our theoretical lectures, we will draw circuit elements connected by wires, and it is very important to understand what these wires mean when we draw them. Specifically, thess are special theoretical "ideal wires". In ideal wires, the voltage *everywhere* in that wire is always the same.

On first sight, this may not seem so strange: in electrostatics, you know that metals are special materials that have the same voltage everywhere inside the surface of the metal: there are never (static) electric field inside metals. If there were, the mobile electrons inside the would flow until they cancel those electric fields. 

Here, our wires are even more special, though, because as we draw them in the circuit, the voltage across the wire is also instantaneously transmitted to the other side. In our schematics, the voltage across anything we draw a "wire" is **always** by definition zero.

```python
:tag: hide-input
:class: centered-output
    
import schemdraw
import schemdraw.elements as elm
from IPython.display import SVG, display
import io

with schemdraw.Drawing() as d:
    R1 = elm.Resistor().dot()
    R2 = elm.Resistor().down().dot()
    L = elm.Line().left().dot()
    elm.SourceV().up().label('10V').dot()
    elm.VoltageLabelArc().at(R1).label(r'$\Delta V_1$')
    elm.VoltageLabelArc().at(R2).label(r'$\Delta V_2$')
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


### Voltages in circuits

Once we have accepted ideal wires as little tunnels that instantaneously equilabrate voltages from one node of the circuit to the other, then life in theoretical circuit analysis becomes realatively simple: we do not need to solve the 3-dimensional partial differential equations that come from Coulomb's law from electrostatics, or Ampere's law from magnetostatics. All of the complexity of your electromagnetism courses is mapped into the voltage dropped across the lumped elements we draw in our circuit.

While this seems like a drastic approximation, it can be highly accurate, and if you are really committed, you can actually rebuild all of 3-dimensional electromagntism by meashing 3-dimensional space into a network of nodes that you connect with (mutual) inductances and capacitances, which is what you actually do when you [solve electromagnetic problems with finite element methods](https://en.wikipedia.org/wiki/Computational_electromagnetics).

### Ohms law

One of the circuit elements you have certainly studied in the past is a [resistor](https://en.wikipedia.org/wiki/Resistor). A resistor is a circuit element which produces a current proportional to the voltage drop across it:

$$
\Delta V = - IR
$$

For our resistor, and also in general for all of the components we will study, the voltage drops between the two nodes of the component and the current flows from one node to the other. The sign is negative because you need to supply a voltage difference in order to get current to flow through the resistor. Note it is important to get the convensions of signs right when you draw this in a circuit: in the equation above, the voltage drop follows the same direction as the current flow:

```python
:tag: hide-input
:class: centered-output
    
with schemdraw.Drawing():
    R = elm.Resistor().down().dot().idot()
    elm.VoltageLabelArc().at(R).label(r'$\Delta$V')
    elm.CurrentLabelInline(direction='in').at(R).label('I')
```

For the choice of convention that the current is flowing downwards, and if we choose to define the bottom of the resistor as ground, then you will get a voltage $V = IR$ at the upper node:

```python
:tag: hide-input
:class: centered-output
    
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

Note that in the convention above, with the direction of the current as shown such that $I$ is a positive number, then $V$ is also a positive number, which gives you the familiar following Ohm's law $V = IR$.

Note that when dealing with resistor, voltages are like the forces that are driving the circuit, analogous to pressure difference that drive water flow in a pipe: you apply a voltage and then you get a current in response. When we study inductors and capacitors, we will encounter similar linear relations between voltages and currents and their integrals / derivatives, and we will follow the same sign convention introduced here.


### Impedance

In the above, we have been talking about resistors, which resist the flow of current following Ohms law. In this course, we will go beyond resistors and consider more general circuit elements such as capacitors and inductors. Unlike resistors, inductors and capacitors do not follow Ohm's law. But the do, in genral, **impede** (prevent / hold back) the free flow of current: capacitors, for example, will block DC currents, but allow AC currents to flow through. And inductors will allow DC currents to flow freely, but will block ("choke") AC currents. 

The fact that all of these elements will at some point potentially block the flow of current will lead us to refer to the way that they do so as their **[**impedance**](https://en.wikipedia.org/wiki/Electrical_impedance)**. 

For an ideal resistor, the only way that it will react to an attempt to flow current through it is by Ohm's law: for a resistor, it's impedance is exactly equal to it's resistance, you can use (and we will use) the two words interchangeably. Note that the resistor has no ability to store energy: all the energy you provide to force current to flow through it is irreversibly lost to heat. 

Inductors and capacitors react differently than resistors if you try to flow current through them: ideal inductors and capacitors will not have any part of their voltage drop given by ohms law, but they will not always let current flow freely. We therefore use the word **impedance** to describe how these react to currents and voltages. Because idealy inductors and capacitors react to voltages and currents in way that they will never dissipate any energy, the impedance of circuits made from inductors and capacitors only is sometimes given the name **[reactance](https://en.wikipedia.org/wiki/Electrical_reactance)**, because they react to voltages and currents but do not dissipate energy. 

Finally, in the most general case, where you have a circuit that contains both inductors, capacitors, and resistors, the total impedance will not be purely resistive, not purely reactive, but a combination of both. 


## Kirchoff's laws

When connecting elements together in circuits, the relation of the voltages at the different nodes and the currents in different branches of the circuit are given by [Kirchoff's Laws](https://en.wikipedia.org/wiki/Kirchhoff%27s_circuit_laws).

### Kirchoff's current law

The first of Kirchoff's laws is related to the conservation of charge. Since the ideal wires we draw in our circuit diagrams have no capacity to hold charge (capacitance), the currents flowing in and out of any node in the circuit must sum up to zero:

```python
:tag: hide-input
:class: centered-output
    
import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    W1 = elm.Line().dot().label("Branch 1", loc="left")
    with d.hold():  # Save this drawing position/direction for later
        W2 = elm.Line().down().label("Branch 2", loc="bottom") 
    W3 = elm.Line().label("Branch 3", loc="right")
    d.add(elm.Dot().at(W3.start).label('Node', loc='top'))


    # Position arrows at the middle of each wire segment using ofst=0.5
    elm.CurrentLabelInline(direction='in', start=False, ofst=0).at(W1).label(r'$I_1$').reverse()
    elm.CurrentLabelInline(direction='in', ofst=0).at(W2).label(r'$I_2$')
    elm.CurrentLabelInline(direction='in', ofst=0).at(W3).label(r'$I_3$')
```

<!-- #region -->
In the schematic here, the three wires are connected at a point in the circuit shown by a dot: this dot is referred to as a **[node](https://en.wikipedia.org/wiki/Node_(circuits))** of the circuit. 

*(We will sometimes explicity draw dots, sometimes not. Dots in CAD drawings of circuits are also often used to explicity indicate that crossing wires are connected. There are [varying conventions](https://upload.wikimedia.org/wikipedia/commons/3/36/Wire_Crossover_Symbols_for_Circuit_Diagrams.png) on this, and you will encounter both, you should try to use some logical thinking to figure out which one is relevant, and ask if you are not sure. In any case, even if there is not a dot, any set of connected wires is always equivalent to a node.)* 

The voltage on each node is also equal to the voltage and on all wires connected to, in that sense, from a voltage point of view, all wires connected to the node are also consider as the the same "node" of the circuit (see this the [image](https://upload.wikimedia.org/wikipedia/commons/9/95/Nodes2.svg) on the [wikipedia page](https://en.wikipedia.org/wiki/Node_(circuits)) for example). 

The wires connected to the node are referred to as [branches](https://en.wikipedia.org/wiki/Nodal_analysis). As you can see in the figure, although the three wires have the same voltage, they can have *different* currents. 

This brings us to **Kirchoff's current law**: the sum of the currents from all branches connected to a node must be zero:

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
<!-- #endregion -->

### Kirchoff's voltage law

The second of Kirchoff's laws tells us about how voltages change as we go through the network of the circuit. While Kirchoff's current law applies to *nodes* in the circuit, **Kirchoff's voltage law** applies to *loops* in the circuit, and states that if you follow a loop around your circuit and come back to the same place, then the sum of all the voltage drops between the nodes $n$ in your loop must be zero:

$$
\sum_{\rm loop} \Delta V_{n+1,n} = 0
$$

Here, one has to be very careful about sign conventions: when applying this formula, you must pick an direction that you will traverse your loop, and the voltage difference $\Delta V_{n+1,n}$ is the change of voltage as you move through your loop in the chosen direction.

Here is a concrete example:

```python
:tag: hide-input
:class: centered-output
    
import schemdraw
import schemdraw.elements as elm
from IPython.display import SVG, display
import io

with schemdraw.Drawing() as d:
    # To do: add node labels!!!! and a circulating arrow
    R1 = elm.Resistor().dot().label("$R_1$")
    R2 = elm.Resistor().down().dot().label("$R_2$")
    R3 = elm.Resistor().left().dot().label("$R_3$")
    S = elm.SourceV().up().dot().label("$V_0$")
    d.add(elm.Dot().at(R1.start).label('$V_2$', loc='top'))
    d.add(elm.Dot().at(R1.end).label('$V_3$', loc='top'))
    d.add(elm.Dot().at(R3.start).label('$V_4$', loc='bottom'))
    d.add(elm.Dot().at(R3.end).label('$V_1$', loc='bottom'))
```

In this case, we have chosen a clockwise direction for a loop, giving the following:

$$
\Delta V_{2,1} + \Delta V_{3,2} + \Delta V_{4,3} + \Delta V_{0,4} = 0
$$

Since we have no branches in this circuit, the same current $I$ must flow through all elements in the loop. Using the volatage-current relation for a resistor, we can then write this as:

$$
V_0 - I R_1 - I R_2 - I R_3 = 0
$$

Note the negative signs in this formula: $\Delta V_{3,2} = -I R_2$ this is because when you follow the direction that the current is flowing in the resistor, the voltage across the resistor in this direction *drops*. The source term, using the terminals as indicated, increases the voltage from node 1 to node 2 by $V_0$, which is why there is no negative sign there in the formula.

Note that we can now directly solve for the current, and therefore also all the voltages, in the circuit:

$$
I = \frac{V_0}{R_1 + R_2 + R_3}
$$


### Series and parallel combinations of resistors

As you can see from the example we just looked at, in the circuit above, if we want to know what the current is, we can replace the three resistors in series with a single equivalent resistor whos value is given by the sum:

$$
R_{\rm s} = \sum_n R_n
$$

If I have two resistors in series $R_1$, and $R_2$, their total equivalent is $R_1 + R2$.

Using Kirchoff's current law, one can also show in a very similar way that for resistors in parallel, the equivalent resistance is given by the sum of the inverse of all the resistances:

$$
\frac{1}{R_{||}} 
= \sum_n 
\frac{1}{R_n} 
$$

If I have two resistor $R_1$ and $R_2$ in parallel, their equivalent resistance is $R_1 || R_2 = R_1 R_2 / (R_1 + R_2)$, where we have introduced the convenient notation $||$ to represent the mathematical operation of taking the inverse of the sum of the inverses. 

These are likely familiar to you already: in this course, you will use these exetensively to redraw and simplify circuits, and will soon extend these concepts to cover the behaviour of arbitrary linear impedances from elements such as inductances and capacitances.


### Example: Applying Kirchoff's laws

To illustrate using Kirchoff's laws to solve more complex circuits, we will consider the following circuit:

```python
:tag: hide-input
:class: centered-output
    
import schemdraw
import schemdraw.elements as elm
from IPython.display import SVG, display
import io

with schemdraw.Drawing() as d:
    # To do: add node labels!!!! and a circulating arrow
    S1 = elm.SourceV().up().label("5V")
    d.add(elm.Dot().at(S1.end).label('$V_1$', loc='top'))
    elm.CurrentLabelInline(direction='out').at(S1).label(r'$I_1$').reverse()
    R1 = elm.Resistor().right().dot().label("2k")
    elm.CurrentLabelInline(direction='out').at(R1).label(r'$I_2$').reverse()
    d.push()
    R2 = elm.Resistor().down().dot().label("3k")
    d.add(elm.Dot().at(R2.start).label('$V_2$', loc='top'))
    d.add(elm.Dot().at(R2.end).label('$V_4$', loc='bottom'))
    elm.CurrentLabelInline(direction='out').at(R2).label(r'$I_3$').reverse()
    d.pop()
    R3 = elm.Resistor().right().dot().label("4k")
    d.add(elm.Dot().at(R3.end).label('$V_3$', loc='top'))
    elm.CurrentLabelInline(direction='out').at(R3).label(r'$I_4$').reverse()
    S2 = elm.SourceV().down().reverse().label("2V")
    elm.CurrentLabelInline(direction='in').at(S2).label(r'$I_5$')
    L1 = elm.Line().left()
    L2 = elm.Line().left()
```

In the diagram, we have labelled all the potentially independent node voltages and branch currents.

We will first use Kirchoff's current law for the branches connected to the four nodes to give us 4 equations:

\begin{align}
I_1 - I_2 & = 0 \\
I_2 - I_3 - I_4 & = 0 \\
I_4 - I_5 & = 0 \\
I_5 + I_3 - I_1 & = 0
\end{align}

We will then use Kirchoff's voltage law to give us two equations for the left and right loops you can see in the drawing, written here for both loops running clockwise:

\begin{align}
(V_1 - V_4) + (V_2 - V_1) + (V_4 - V_2) & = 0 \\
(V_2 - V_4) + (V_3 - V_2) + (V_4 - V_3) & = 0
\end{align}

What about the outer loop? We could also use the voltage law to write down an equation for that loop, but it would not give us independent information: it would reduce to one of the two equations above upon substitution. In order to generate *independent* equations from Kirchoff's voltage law, you should write out equations using only [independent meshes](https://en.wikipedia.org/wiki/Mesh_analysis) consistent of loops that do not contain any other loops. 

*(The page on linked above on mesh analysis also provides an useful alternative approach using mesh loop currents rather than branch currents, based using the superposition principle, can make it faster to generate a minimal set of equations from Kirchoff's laws, see the section on the superposition principle below.)*

We now have 6 equations and 9 unknowns. There are three more things that we can use:

* The two voltage sources give the same voltage drop *independent* of how much current is flowing through them: this eliminates two unknowns, bringing us to 6 equations and 7 unknowns
* The absolute voltage does not matter (we can choose one point to be [ground](https://en.wikipedia.org/wiki/Ground_(electricity)) if we like), leaving us with 6 equations and 6 unknowns.

Using Ohm's law for the resistors, we can then write all of the equations in terms of current, and by substituting equations into each other to eliminate varibles one by one, we can solve for all branch currents and node voltages.


## The superposition principle

As you may have noticed, the equations describing Kirchoff's laws are all linear equations (linear in the branch currents and node voltages). A very useful consequence of this is that we can use the [superposition principle](link) to simplfiy and solve circuits: for a different set of values of the sources, the solution of the sum of different source values is the sum of the solutions. We will consider the same circuit as above:

```python
:tag: hide-input
:class: centered-output
    
import schemdraw
import schemdraw.elements as elm
from IPython.display import SVG, display
import io

with schemdraw.Drawing() as d:
    # To do: add node labels!!!! and a circulating arrow
    S1 = elm.SourceV().up().label("5V")
    d.add(elm.Dot().at(S1.end).label('$V_1$', loc='top'))
    elm.CurrentLabelInline(direction='out').at(S1).label(r'$I_1$').reverse()
    R1 = elm.Resistor().right().dot().label("2k")
    elm.CurrentLabelInline(direction='out').at(R1).label(r'$I_2$').reverse()
    d.push()
    R2 = elm.Resistor().down().dot().label("3k")
    d.add(elm.Dot().at(R2.start).label('$V_2$', loc='top'))
    d.add(elm.Dot().at(R2.end).label('$V_4$', loc='bottom'))
    elm.CurrentLabelInline(direction='out').at(R2).label(r'$I_3$').reverse()
    d.pop()
    R3 = elm.Resistor().right().dot().label("4k")
    d.add(elm.Dot().at(R3.end).label('$V_3$', loc='top'))
    elm.CurrentLabelInline(direction='out').at(R3).label(r'$I_4$').reverse()
    S2 = elm.SourceV().down().reverse().label("2V")
    elm.CurrentLabelInline(direction='in').at(S2).label(r'$I_5$')
    elm.Line().left()
    elm.Line().left()
    
```

A second approach to solve this kind of circuit is to use the principle of superposition. Using the superposition principle, we can solve this in two steps: First, set the right hand voltage source to zero volts. We will call this scenario "A" of our superposition calculation. The circuit that results is the following:

```python
:tag: hide-input
:class: centered-output
    
import schemdraw
import schemdraw.elements as elm
from IPython.display import SVG, display
import io

with schemdraw.Drawing() as d:
    # To do: add node labels!!!! and a circulating arrow
    S1 = elm.SourceV().up().label("5V")
    d.add(elm.Dot().at(S1.end).label('$V_1^A$', loc='top'))
    elm.CurrentLabelInline(direction='out').at(S1).label(r'$I_1^A$').reverse()
    R1 = elm.Resistor().right().dot().label("2k")
    d.push()
    R2 = elm.Resistor().down().dot().label("3k")
    elm.Ground()
    d.add(elm.Dot().at(R2.start).label('$V_2^A$', loc='top'))
    elm.CurrentLabelInline(direction='out').at(R2).label(r'$I_3^A$').reverse()
    d.pop()
    R3 = elm.Resistor().right().label("4k")
    elm.CurrentLabelInline(direction='out').at(R3).label(r'$I_4^A$').reverse()
    elm.Line().down()
    elm.Line().left()
    elm.Line().left()
    
```

In drawing the above, we have already used current conservation at the upper left node to remove one of the current variables and we have defined a ground to remove one of the voltage node variables, leaving us with 3 branch current variables and two node voltage variables. We have kept the same numbering of the variables because later we will need to add them in the two scenarios to get the final values lined up with the initial circuit.

With our choice of ground, we can use the behaviour of the votlage source to already see that $V_1^A = 5V$. 

We can use the shortcuts of parallel and series combinations to find some answers pretty quickly: the current $I_1^A$ is given by: 

$$
I_1^A = \frac{5 \rm V}{2k + 4k||3k} \approx 1.34\ {\rm mA}
$$

We can then immediately find $V_2^A$:

$$
V_2^A = 5V - I_1^A R_{2k} \approx 2.30\ {\rm V}
$$

And from there we can also easily find the current through the last two resistors, giving $I_3^A \approx 0.77$ mA and $I_4^A \approx 0.58$ mA.

The second step is to repeat the analysis but then replacing the left hand voltage by 0V:

```python
:tag: hide-input
:class: centered-output
    
import schemdraw
import schemdraw.elements as elm
from IPython.display import SVG, display
import io

with schemdraw.Drawing() as d:
    # To do: add node labels!!!! and a circulating arrow
    S1 = elm.Line().up()
    elm.CurrentLabelInline(direction='out').at(S1).label(r'$I_1^B$').reverse()
    R1 = elm.Resistor().right().dot().label("2k")
    d.push()
    R2 = elm.Resistor().down().dot().label("3k")
    elm.Ground()
    d.add(elm.Dot().at(R2.start).label('$V_2^B$', loc='top'))
    elm.CurrentLabelInline(direction='out').at(R2).label(r'$I_3^B$').reverse()
    d.pop()
    R3 = elm.Resistor().right().dot().label("4k")
    d.add(elm.Dot().at(R3.end).label('$V_3^B$', loc='top'))
    elm.CurrentLabelInline(direction='out').at(R3).label(r'$I_4^B$').reverse()
    S2 = elm.SourceV().down().reverse().label("2V")
    elm.Line().left()
    elm.Line().left()
    
```

Now, we have a similar relatively simple situation, although we will have to be careful with the sign conventions of our current. 

We can see already that we will have $V_3^B = 2$ V. The current $I_4$ here will actually flow in the opposite direction (it will be negative) and will have the value:

$$
I_4^B = - \frac{2\ \rm V}{4k + 2k || 3k} \approx -0.38\ {\rm mA}
$$


And similarly, we can then find $V_2^B$ (note again to be careful with the sign conventions):

$$
V_2^B = 2V + I_4^B R_{4k} \approx 2 + (-0.38\ {\rm mA})\times(4000) = 0.46\ {\rm V}
$$


Given then $I_3^B = 0.15$ mA and $I_1^B = -0.23$ mA (note negative sign again on the current due to our initially chosen sign convention).


We then use the superposition principle: the value of any branch current or node voltage is equal to the sum of the values we found in situation A and situation B. For example:

$$
I_1 = I_1^A + I_1^B = (1.34 - 0.23)\ {\rm mA} = 1.11\ {\rm mA}
$$

and:

$$
V_2 = V_2^A + V_2^B = (2.30 + 0.46)\ {\rm V} = 2.76\ {\rm V}
$$


While it is more steps, the algebra is simpler in this case if we use the superposition principle, and importantly, the *idea* of being able to use the superposition principle is quite conceptually important, particularly when we start to look at small signal analysis later in the course.

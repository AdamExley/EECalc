<!-- This section will be included in ~/README.md -->
<!-- START-PLANNED-FEATURES -->

# Planned Features

**🔵Core Features** <br>
**🔷<span style="color:#077d15">Priority Features</span>**<br>
**🔹<span style="color:#a68723">Eventual Features</span>**<br>
**🔸<span style="color:#cc7229">Possible Features</span>**<br>
**🔻<span style="color:#c9401e">A **bit** down the road but I'm *tempted*</span>**<br>


## Organization
- [ ] **🔵Projects:** Stored as directories with human-readable-ish data
    - [ ] **🔸<span style="color:#cc7229">Power Rail Configuration</span>:** Store available power rails with tolerance, stability, and use preference.
        - [ ] **🔻<span style="color:#c9401e">Load Estimation</span>:** Use calculators and other contributions to figure out power loads.
- [ ] **🔵(sub)Circuits:** Organize your calculations within a project!
    - [ ] **🔷<span style="color:#077d15">Reuse</span>:** Use a circuit within another circuit (subcircuits)
        - [ ] **🔻<span style="color:#c9401e">Dependent Optimization</span>:** Optimize two subcircuits to work together, accounting for factors like loading.
- [ ] **🔵Try-Then-Commit:** Tinker with any value, use it in other circuits, and **then** choose to change things up.



## All Components:
- [ ] **🔵Global Part Library:** Save characteristics and information about parts to reuse them.
    - [ ] **🔵Internal Naming:** Add aliases for parts (i.e. Company Part Numbers).
    - [ ] **🔹<span style="color:#a68723">Double Click to Add</span>:** See a generic 1kΩ 0402? You'll probably use a lot of those, so it should be easy to add it to your custom library.
- [ ] **🔷<span style="color:#077d15">Project Library</span>:** See what parts you're already using in a project (and prefer them).
- [ ] **🔻<span style="color:#c9401e">Complex Nonlinearities and Nonidealities</span>:** Amplitude dependence, bias dependence, anything that pushes math far out of the S-domain.



## Basic Passive Components (RLC)
- [ ] **🔵Standardization:** Automatic respect of the E-series using `eseries` for any automatic calculations.
- [ ] **🔵Tolerancing** 
- [ ] **🔷<span style="color:#077d15">Prioritization</span>:** Let's keep BOM lines down, if a part's in your project library or global library, let's see if we can make it work.
- [ ] **🔷<span style="color:#077d15">A sense of reality</span>:** A `1F` SMD capacitor doesn't exist. This won't suggest one.
- [ ] **🔹<span style="color:#a68723">Parasitics</span>:** Basic user-defined RLC parasitics.
    - [ ] **🔹<span style="color:#a68723">Estimation</span>:** Estimation of standard package (0201, 0402, ...) parasitics.

## Other Component Support
- [ ] **🔹<span style="color:#a68723">Ferrite Beads</span>** (with parameter extraction)
- [ ] **🔹<span style="color:#a68723">Opamps</span>** 
- [ ] **🔻<span style="color:#c9401e">Diodes</span>**
- [ ] **🔸<span style="color:#cc7229">Black Box Sources</span>:** VCVS, VCCS, CCVS, CCCS
- [ ] **🔸<span style="color:#cc7229">Static Subcircuits</span>**




## Actual Calculators and Utilities
- [ ] **🔵Resistor Combination:** Parallel / series to hit specific tolerance and/or power rating. Ala [jansson.us](https://jansson.us/resistors.html)
- [ ] **🔵Capacitor Combination:** Parallel / series to hit specific tolerance and/or voltage rating.
- [ ] **🔵Inductor Combination:** Parallel / series to hit specific tolerance and/or current rating.
- [ ] **🔵Opamp Gain/Offset Circuits:** I manually use [TI's Designing Gain and Offset in 30s](https://www.ti.com/lit/an/sloa097/sloa097.pdf?ts=1755961810243&ref_url=https%253A%252F%252Fwww.google.com%252F) far too much *(and it usually takes me more than 30s)*
    - [ ] **🔷<span style="color:#077d15">Worst-Case Analysis</span>**
- [ ] **🔷<span style="color:#077d15">Plot Digitizer</span>:** Ala [WebPlotDigitizer](https://plotdigitizer.com/), but tailored down for datasheet translation *(and for sanity during development)*.
- [ ] **🔷<span style="color:#077d15">Filter Designer</span>:** Topologies TBD.
    - [ ] **🔹<span style="color:#a68723">Worst-Case Analysis</span>**
    - [ ] **🔸<span style="color:#cc7229">Side-by-Side Comparison</span>**
- [ ] **🔻<span style="color:#c9401e">Custom Metrics</span>:** Create your own performance criteria.




# Some More Details

### Calculation Methods
- **(Preferred)** Analytical calculation, where reasonable, using `SymPy` and `Lcapy`
- *Light* SPICE simulation using `PySpice` with an `Ngspice` backend
    - Limited to Small Signal, Noise, and *maybe* some AC Large Signal.



<!-- END-PLANNED-FEATURES -->





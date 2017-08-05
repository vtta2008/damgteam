//Maya ASCII 2017ff04 scene
//Name: test1.ma
//Last modified: Sat, May 13, 2017 06:22:18 AM
//Codeset: 1252
requires maya "2017ff04";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2017";
fileInfo "version" "2017";
fileInfo "cutIdentifier" "201702071345-1015190";
fileInfo "osv" "Microsoft Windows 8 Home Premium Edition, 64-bit  (Build 9200)\n";
createNode transform -n "Cube_Nurbs_on_base";
	rename -uid "65917B91-4B9D-BBD9-8200-CA800D47B7C5";
createNode nurbsCurve -n "Cube_Nurbs_on_baseShape" -p "Cube_Nurbs_on_base";
	rename -uid "9D4F2B32-4147-2BC8-BB59-468EF9585C70";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-0.56929782976144139 1.1385956595228828 -0.56929782976144139
		-0.56929782976144139 1.1385956595228828 0.56929782976144139
		0.56929782976144139 1.1385956595228828 0.56929782976144139
		0.56929782976144139 1.1385956595228828 -0.56929782976144139
		-0.56929782976144139 1.1385956595228828 -0.56929782976144139
		-0.56929782976144139 0 -0.56929782976144139
		0.56929782976144139 0 -0.56929782976144139
		0.56929782976144139 1.1385956595228828 -0.56929782976144139
		0.56929782976144139 1.1385956595228828 0.56929782976144139
		0.56929782976144139 0 0.56929782976144139
		0.56929782976144139 0 -0.56929782976144139
		-0.56929782976144139 0 -0.56929782976144139
		-0.56929782976144139 0 0.56929782976144139
		0.56929782976144139 0 0.56929782976144139
		0.56929782976144139 1.1385956595228828 0.56929782976144139
		-0.56929782976144139 1.1385956595228828 0.56929782976144139
		-0.56929782976144139 0 0.56929782976144139
		;
createNode transform -n "Spike_Cross_Control";
	rename -uid "338EB20B-4868-321C-6BBB-4698581216E6";
createNode nurbsCurve -n "Spike_Cross_ControlShape" -p "Spike_Cross_Control";
	rename -uid "D853039C-4FFC-327A-D09E-3384485EE092";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 20;
	setAttr ".cc" -type "nurbsCurve" 
		1 39 0 no 3
		40 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39
		40
		0.56982715083383706 4.0911216636629888e-009 -2.1328837350509389e-005
		0.42089523917311311 0.14888739445176391 -1.5755096100633637e-005
		0.27209314192421008 4.0735560498550427e-005 -1.0184545420344193e-005
		0.42093980071123838 -0.14876136179267441 -1.5755096101521815e-005
		0.56982715083383706 4.0911216636629888e-009 -2.1328837350509389e-005
		0.42091194939160675 6.3015495567864122e-005 -0.14884013478191349
		0.27209314192421008 4.0735560498550427e-005 -1.0184545420344193e-005
		0.42092309049279564 6.3017163522971487e-005 0.14880862458971134
		0.56982715083383706 4.0911216636629888e-009 -2.1328837350509389e-005
		0.42089523917311311 0.14888739445176391 -1.5755096100633637e-005
		0.27209314192421008 4.0735560498550427e-005 -1.0184545420344193e-005
		-0.27209312915292649 -0.00012604132942328761 1.0184545417679658e-005
		-0.4209971894939688 -6.3028257021535694e-005 0.14884013797247952
		-0.56982713806255436 -8.5309860045956754e-005 2.1328837348733032e-005
		-0.4210083305952077 -6.3029924976643059e-005 -0.14880862139914619
		-0.27209312915292649 -0.00012604132942328761 1.0184545417679658e-005
		-0.42085456057731463 0.14876116408473417 1.5751905531047328e-005
		-0.56982713806255436 -8.5309860045956754e-005 2.1328837348733032e-005
		-0.42098047927552518 -0.14888740721321847 1.5758286666667232e-005
		-0.27209312915292649 -0.00012604132942328761 1.0184545417679658e-005
		-0.27209312915292649 -0.00012604132942328761 1.0184545417679658e-005
		0 -1.3322676295501878e-015 0
		-1.1141101238898443e-005 -1.6679564396326896e-009 0.27211440318025648
		0.00014271626145045957 0.14882419235483146 0.42093877648166433
		0 -1.3322676295501878e-015 0.56976316255188397
		1.6710218443627411e-005 -0.14882437895619827 0.42093878286606934
		-1.1141101238898443e-005 -1.6679564396326896e-009 0.27211440318025648
		-0.14882987953462568 -2.2281592690021057e-005 0.42094435341416769
		0 -1.3322676295501878e-015 0.56976316255188397
		0.14890412937122033 -6.29878057401001e-005 0.42093320912223664
		-1.1141101238898443e-005 -1.6679564396326896e-009 0.27211440318025648
		-3.1511783191717768e-005 -4.7176880180188618e-009 -0.27211440158374511
		-5.9356788792541693e-005 0.14882437257149927 -0.42093878126979423
		-4.2652884430616211e-005 -6.3856417931162923e-009 -0.56976316095537172
		-1.4801564748090357e-005 -0.14882438367388451 -0.42093878126955797
		-3.1511783191717768e-005 -4.7176880180188618e-009 -0.27211440158374511
		-0.14886139131781739 -2.2286310378039076e-005 -0.42093321072146139
		-4.2652884430616211e-005 -6.3856417931162923e-009 -0.56976316095537172
		0.14887261758802861 -6.299252342767403e-005 -0.42094435501339156
		-3.1511783191717768e-005 -4.7176880180188618e-009 -0.27211440158374511
		;
select -ne :time1;
	setAttr ".o" 1;
	setAttr ".unw" 1;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -s 2 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 4 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultRenderGlobals;
	setAttr ".ren" -type "string" "renderManRIS";
	setAttr ".pram" -type "string" "pgYetiVRayPreRender";
	setAttr ".poam" -type "string" "pgYetiVRayPostRender";
	setAttr ".prlm" -type "string" "pgYetiPrmanFlush";
	setAttr ".polm" -type "string" "pgYetiPrmanFlush";
	setAttr ".prm" -type "string" "";
	setAttr ".pom" -type "string" "pgYetiPrmanFlush";
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
select -ne :ikSystem;
	setAttr -s 4 ".sol";
// End of test1.ma

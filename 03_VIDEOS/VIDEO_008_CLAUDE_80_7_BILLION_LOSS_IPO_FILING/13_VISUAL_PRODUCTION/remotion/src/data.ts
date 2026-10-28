export type Graphic = {
  scene: string;
  eyebrow: string;
  title: string;
  note: string;
  kind: 'rows' | 'flow' | 'timeline' | 'bars' | 'columns' | 'split' | 'matrix';
  items: {label: string; value: string; accent?: boolean}[];
};

export const graphics: Graphic[] = [
  {scene:'SC002',eyebrow:'H1 2026 · SEC S-1',title:'THE LOSS WAS NOT THE OPERATION',note:'GAAP and operating results are different measures.',kind:'rows',items:[{label:'GAAP NET LOSS',value:'−$80.748B',accent:true},{label:'FAIR-VALUE CHANGE',value:'−$72.388B'},{label:'OPERATING LOSS',value:'−$0.693B'}]},
  {scene:'SC007',eyebrow:'OCTOBER 26, 2026',title:'ONE DAY. TWO DISCLOSURES.',note:'Times and sources remain separately attributed.',kind:'timeline',items:[{label:'SEC ACCEPTANCE',value:'09:00 ET'},{label:'PARTNERS ANNOUNCEMENT',value:'16:15 ET',accent:true}]},
  {scene:'SC010',eyebrow:'FINANCING STRUCTURE',title:'THE MONEY DOES NOT GO TO ANTHROPIC',note:'Funding and rent are different flows.',kind:'flow',items:[{label:'FINANCIERS',value:'CAPITAL'},{label:'SPV',value:'BUYS EQUIPMENT',accent:true},{label:'ANTHROPIC',value:'LEASES CAPACITY'}]},
  {scene:'SC015',eyebrow:'REVENUE · FIRST HALF',title:'RAPID GROWTH, SAME UNIT',note:'Observed revenue, not a forecast.',kind:'bars',items:[{label:'H1 2025',value:'$1.163B'},{label:'H1 2026',value:'$16.286B',accent:true}]},
  {scene:'SC020',eyebrow:'ANNOUNCED EQUIPMENT FINANCING',title:'$63 BILLION',note:'Financing for equipment — not a cash deposit to Anthropic.',kind:'rows',items:[{label:'PURPOSE',value:'AI COMPUTE EQUIPMENT'},{label:'VEHICLE',value:'SPECIAL-PURPOSE VEHICLE'},{label:'STATUS',value:'ANNOUNCED',accent:true}]},
  {scene:'SC029',eyebrow:'LEASE MECHANICS',title:'PAYMENTS FOLLOW READY-FOR-SERVICE',note:'Not all five years of rent were due at filing.',kind:'timeline',items:[{label:'DELIVERY',value:'EQUIPMENT'},{label:'READY FOR SERVICE',value:'START'},{label:'QUARTERLY',value:'LEASE PAYMENTS',accent:true}]},
  {scene:'SC036',eyebrow:'DO NOT ADD THESE NUMBERS',title:'TWO DIFFERENT DISCLOSURES',note:'The degree of overlap is not established.',kind:'split',items:[{label:'GROSS FIVE-YEAR RENT',value:'~$125.2B'},{label:'ANNOUNCED FINANCING',value:'$63B',accent:true}]},
  {scene:'SC040',eyebrow:'CAPITAL STACK',title:'DIFFERENT LAYERS. DIFFERENT ROLES.',note:'No percentages are inferred.',kind:'rows',items:[{label:'FIRST LIEN',value:'BANK ARRANGERS'},{label:'SECOND LIEN',value:'BLACKSTONE PORTION',accent:true}]},
  {scene:'SC045',eyebrow:'WHAT WAS ACTUALLY ANNOUNCED',title:'ANNOUNCEMENT IS NOT DELIVERY',note:'Future utilization and sales remain unknown.',kind:'timeline',items:[{label:'2026',value:'ANNOUNCED'},{label:'2027',value:'EXPECTED DELIVERIES',accent:true},{label:'FUTURE',value:'USE UNKNOWN'}]},
  {scene:'SC055',eyebrow:'THREE SEPARATE CATEGORIES',title:'NO SINGLE DEBT TOTAL',note:'Different dates, terms and economic meaning.',kind:'columns',items:[{label:'CONDITIONAL NOTES',value:'FINANCING'},{label:'EQUIPMENT RENT',value:'LEASES',accent:true},{label:'CUSTOMER REVENUE',value:'OPERATIONS'}]},
  {scene:'SC059',eyebrow:'H1 2026 · USD BILLIONS',title:'THE OPERATING BRIDGE',note:'Rounded figures from the SEC filing.',kind:'flow',items:[{label:'REVENUE',value:'$16.286B'},{label:'OPERATING EXPENSE',value:'−$16.979B',accent:true},{label:'OPERATING RESULT',value:'−$0.693B'}]},
  {scene:'SC064',eyebrow:'DIFFERENT NATURE · DIFFERENT PERIOD',title:'ACCOUNTING CHARGE ≠ FUTURE RENT',note:'Neither figure may be treated as the other.',kind:'split',items:[{label:'REPORTED H1 CHARGE',value:'FAIR VALUE'},{label:'FUTURE EXPOSURE',value:'LEASE TERM',accent:true}]},
  {scene:'SC069',eyebrow:'PROPOSED IPO GOVERNANCE',title:'VOTES ARE NOT ECONOMIC OWNERSHIP',note:'Governance rights are described conditionally.',kind:'split',items:[{label:'GENERAL VOTING POWER',value:'CLASS F'},{label:'ECONOMIC RIGHTS',value:'SEPARATE',accent:true}]},
  {scene:'SC073',eyebrow:'GOVERNANCE STRUCTURE',title:'TWO CONTROL CHANNELS',note:'Subject to disclosed conditions.',kind:'flow',items:[{label:'CLASS F SHARE',value:'50.1% GENERAL VOTES'},{label:'BOARD',value:'BUSINESS OVERSIGHT',accent:true},{label:'CLASS T / LTBT',value:'DIRECTOR ELECTIONS'}]},
  {scene:'SC078',eyebrow:'CONDITION PRECEDENT',title:'FILING DOES NOT MEAN CLOSING',note:'The governance outcome depends on an IPO closing.',kind:'timeline',items:[{label:'PRELIMINARY',value:'S-1 FILED'},{label:'IF COMPLETED',value:'IPO CLOSE',accent:true},{label:'THEN',value:'SPECIFIED GOVERNANCE'}]},
  {scene:'SC080',eyebrow:'PROPOSED GOVERNANCE MATRIX',title:'VOTING AND OVERSIGHT ARE DISTINCT',note:'No automatic operating-control claim.',kind:'matrix',items:[{label:'SHAREHOLDER VOTE',value:'CLASS F · 50.1%'},{label:'BUSINESS OVERSIGHT',value:'BOARD'},{label:'DIRECTOR ELECTIONS',value:'CLASS T / LTBT',accent:true}]},
  {scene:'SC090',eyebrow:'EVIDENCE BOUNDARY',title:'KNOWN IS NOT THE SAME AS PREDICTED',note:'The filing supports facts, not outcomes.',kind:'split',items:[{label:'SUPPORTED',value:'DISCLOSURES · TERMS'},{label:'UNKNOWN',value:'DEMAND · IPO OUTCOME',accent:true}]},
  {scene:'SC094',eyebrow:'SEQUENCE, NOT GUARANTEE',title:'FUNDING → EQUIPMENT → UNKNOWN SALES',note:'Expected delivery does not guarantee demand.',kind:'flow',items:[{label:'$63B',value:'ANNOUNCED FUNDING'},{label:'2027',value:'EXPECTED EQUIPMENT',accent:true},{label:'FUTURE',value:'SALES UNKNOWN'}]},
  {scene:'SC098',eyebrow:'TWO CLOCKS',title:'PAST RESULT. FUTURE TERM.',note:'Do not collapse different periods.',kind:'split',items:[{label:'H1 2026',value:'OPERATING RESULT'},{label:'FIVE YEARS',value:'RENTAL TERM',accent:true}]},
  {scene:'SC104',eyebrow:'FINAL ACCOUNTING CHECK',title:'THREE ROWS. THREE MEANINGS.',note:'The fair-value change is not cash operating spend.',kind:'rows',items:[{label:'GAAP NET LOSS',value:'−$80.748B',accent:true},{label:'OPERATING LOSS',value:'−$0.693B'},{label:'FAIR-VALUE CHANGE',value:'−$72.388B'}]},
  {scene:'SC108',eyebrow:'CONDITIONAL IPO GOVERNANCE',title:'GENERAL VOTES ≠ DIRECTOR ELECTIONS',note:'Simplified from filed agreements; no directorship claim.',kind:'split',items:[{label:'FOUNDER LLC / CLASS F',value:'GENERAL VOTES'},{label:'LTBT / CLASS T',value:'DIRECTOR ELECTIONS',accent:true}]}
];

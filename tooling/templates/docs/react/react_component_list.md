# React Component List

This document will help you understand how to get information about the existing React components that exist in this application.

### Component Documentation

Each component will have a `README.md` file that provides documentation on its use, its props, and any other relevant information. Use this documentation to understand how to leverage these components.

## Features

Features are larger components that encapsulate a specific functionality or section of the application. They may consist of multiple widgets and are typically used to build out the main parts of the user interface. These items are not always reusable, but they are designed to be self-contained and provide a specific set of functionalities.

### Feature Location

In this workspace, you will find features in the following folder location:
`frontend/ReactWebApp/{application_name}/src/app/features`

### Available Features

| Component              | Category   | Tags                                    | Description                                                          | README                                            |
| ---------------------- | ---------- | --------------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------- |
| alerts                 | feedback   | alert,snackbar,notification,feedback    | Global alert and notification system                                 | src/app/features/alerts/README.md                 |
| componenterrorboundary | error      | error,boundary,exception,catch,wrapper  | Reusable error boundary for individual components, customizable UI   | src/app/features/componenterrorboundary/README.md |
| footer                 | navigation | footer,datetime,breadcrumbs,responsive  | Application footer with date, time, and navigation breadcrumbs       | src/app/features/footer/README.md                 |
| genericerror           | feedback   | error,boundary,exception,catch          | Global error boundary for catching JavaScript errors                 | src/app/features/genericerror/README.md           |
| header                 | navigation | header,navbar,branding,menu,auth,search | Main application navigation bar                                      | src/app/features/header/README.md                 |
| nestedmenu             | navigation | menu,nested,submenu,hierarchy           | Enhanced MenuItem component supporting hierarchical menu structures  | src/app/features/nestedmenu/README.md             |
| tiledmenu              | navigation | menu,grid,tiles,navigation,resize,redux | Dynamic grid-based menu with hierarchical navigation and tile sizing | src/app/features/tiledmenu/README.md              |

## Widgets

Widgets are reusable components that can be used across different parts of the application. They are designed to be modular and can be easily integrated into various pages or sections.

### Widget Location

In this workspace you will find widgets in the following folder location

`frontend/ReactWebApp/{application_name}/src/app/widgets`

### Widget Documentation

Each widget will have a `README.md` file that provides documentation on how to use the widget, its props, and any other relevant information. Use this documentation to understand how to leverage this widget.

### Available Widgets

| Component              | Category   | Tags                                                 | Description                                                                           | README                                           |
| ---------------------- | ---------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------ |
| banner                 | display    | banner,info,shimmer,announcement                     | Customizable banner for info/alerts, supports shimmer animation                       | src/app/widgets/banner/README.md                 |
| breadcrumbs            | navigation | breadcrumbs,navigation,location,buttons              | Navigation aid showing hierarchical location with clickable buttons                   | src/app/widgets/breadcrumbs/README.md            |
| buttonbar              | input      | button,toolbar,actions,group                         | Horizontal grouping of action buttons using MUI ButtonGroup                           | src/app/widgets/buttonbar/README.md              |
| cardheader             | display    | card,header,dialog,panel,styling                     | Standardized header for cards, dialogs, panels                                        | src/app/widgets/cardheader/README.md             |
| confirmationdialog     | dialog     | dialog,confirmation,checkbox,acknowledgment          | Standardized confirmation dialogs with simple and checkbox-based variants             | src/app/widgets/confirmationdialog/README.md     |
| contentbase            | layout     | layout,header,actions,content                        | Standardized layout with header, info fields, actions, content                        | src/app/widgets/contentbase/README.md            |
| countOption            | input      | counter,increment,decrement,bounded                  | Numeric counter with plus/minus, boundary enforcement                                 | src/app/widgets/countOption/README.md            |
| customtooltip          | feedback   | tooltip,recharts,visualization,datapoint             | Enhanced tooltip for Recharts charts and data visualizations                          | src/app/widgets/customtooltip/README.md          |
| datagridtooltip        | dialog     | tooltip,datagrid,cell,content,display,feedback       | Specialized tooltip for MUI data grids displaying full text of truncated cell content | src/app/widgets/datagridtooltip/README.md        |
| detailsDialog          | dialog     | dialog,details,info,modal,adaptive                   | Adaptive dialog component for displaying detailed information                         | src/app/widgets/detailsDialog/README.md          |
| gantchart              | chart      | gantt,bar,timeline,state,visualization               | Horizontal bar chart for time-based state/process visualization                       | src/app/widgets/gantchart/README.md              |
| gaugebarchart          | chart      | bar,gauge,vertical,metrics,visualization             | Vertical bar chart for categorical data, metrics, comparisons                         | src/app/widgets/gaugebarchart/README.md          |
| gaugedial              | chart      | gauge,dial,visualization,recharts,fetch,interval     | Gauge dial chart with optional data fetch/refresh, Recharts Pie support               | src/app/widgets/gaugedial/README.md              |
| gaugepiechart          | chart      | gauge,pie,chart,visualization,proportion,legend      | Circular pie chart for proportional data, interactive, customizable, Recharts-based   | src/app/widgets/gaugepiechart/README.md          |
| gaugestackedchart      | chart      | gauge,stacked,bar,chart,visualization,legend         | Horizontal stacked bar chart for composition/resource breakdowns, Recharts-based      | src/app/widgets/gaugestackedchart/README.md      |
| gridperson             | display    | user,person,info,tooltip,graph                       | User information display component with Microsoft Graph Toolkit integration           | src/app/widgets/gridperson/README.md             |
| input                  | input      | input,form,field,autocomplete,datepicker,numeric     | Reusable input components: text, autocomplete, date, numeric, label, validation       | src/app/widgets/input/README.md                  |
| loadingindicator       | feedback   | loading,progress,overlay,spinner                     | Standardized loading overlay with centered spinner, for any container                 | src/app/widgets/loadingindicator/README.md       |
| loadingindicatorbutton | feedback   | loading,button,progress,spinner                      | Loading indicator for use inside buttons, overlays spinner during async actions       | src/app/widgets/loadingindicatorbutton/README.md |
| locationindicator      | display    | location,header,preferences,auth                     | Displays user/machine location in header, based on preferences/auth                   | src/app/widgets/locationindicator/README.md      |
| messageDialog          | dialog     | dialog,message,info,confirmation                     | Simple informational dialog with title, message, and single confirmation button       | src/app/widgets/messageDialog/README.md          |
| multiselect            | input      | multiselect,checkbox,form,filter                     | Checkbox group for multi-selection in forms/filters, supports required/error/disabled | src/app/widgets/multiselect/README.md            |
| optionsDrawer          | navigation | drawer,options,mobile,shortcuts                      | Swipeable bottom drawer for mobile interfaces                                         | src/app/widgets/optionsDrawer/README.md          |
| optionsSelector        | input      | selector,dropdown,options,quick-cycle,shortcuts      | Dropdown selector with optional quick-cycle button and keyboard shortcuts             | src/app/widgets/optionsSelector/README.md        |
| overlay                | display    | overlay,modal,blocking,absolute,centered             | Absolute-positioned overlay for modals, loading, or blocking interaction              | src/app/widgets/overlay/README.md                |
| paceweektodate         | chart      | pace,bar,week,performance,progress,target            | Horizontal bar chart for week-to-date performance, target-based color coding          | src/app/widgets/paceweektodate/README.md         |
| pacingchart            | chart      | pace,bar,performance,actual,target,comparison        | Combined text/bar chart for actual vs. target performance, percent calc, responsive   | src/app/widgets/pacingchart/README.md            |
| pacingchartvert        | chart      | pace,bar,vertical,performance,actual,target          | Vertical bar chart for pacing data, actual vs. target, responsive, reference lines    | src/app/widgets/pacingchartvert/README.md        |
| peoplepicker           | input      | peoplepicker,select,user,assignment,form             | Component for selecting one or more people from a list for user assignment            | src/app/widgets/peoplepicker/README.md           |
| printerdetails         | dialog     | printer,details,info,configuration                   | Component displaying detailed information and configuration options                   | src/app/widgets/printerdetails/README.md         |
| reportviewer           | display    | report,viewer,pdf,table,datagrid                     | Component for displaying reports including PDFs and data tables                       | src/app/widgets/reportviewer/README.md           |
| responsiveFooter       | navigation | footer,responsive,adaptive,floating                  | Adaptive footer component with floating and standard modes                            | src/app/widgets/responsiveFooter/README.md       |
| saveCancelButtons      | input      | save,cancel,buttons,form,dialog                      | Standardized Save and Cancel buttons with state-aware appearance                      | src/app/widgets/saveCancelButtons/README.md      |
| scanner                | input      | scanner,barcode,qr,redux,scan                        | Standardized barcode/QR code scanning interface with Redux integration                | src/app/widgets/scanner/README.md                |
| screenbasefilter       | layout     | layout,filter,content,mobile,desktop                 | Layout for screens with filter panel and content, responsive for mobile/desktop       | src/app/widgets/screenbasefilter/README.md       |
| sectionheader          | display    | section,header,form,alignment                        | Standardized header for sections in pages/forms, flexible alignment/sizing            | src/app/widgets/sectionheader/README.md          |
| selectAndClick         | input      | select,dropdown,button,action                        | Combined dropdown selector with action button for item selection                      | src/app/widgets/selectAndClick/README.md         |
| selectAndPrint         | input      | select,dropdown,print,button,printer                 | Specialized widget combining printer selection dropdown with print button             | src/app/widgets/selectAndPrint/README.md         |
| selectioncardbase      | input      | card,selection,icon,click,overlay                    | Card for labeled values with icon and click overlay, filter/selection UIs             | src/app/widgets/selectioncardbase/README.md      |
| sortOrderButtonGroup   | input      | sort,order,button,group,loading,tooltip              | Standardized up/down button pair for reordering list items                            | src/app/widgets/sortOrderButtonGroup/README.md   |
| table                  | table      | table,datagrid,grid,keyboard,contextmenu,styling     | Robust DataGrid components built on MUI's DataGridPro with keyboard navigation        | src/app/widgets/table/README.md                  |
| timeserieslinegraph    | chart      | line,timeseries,trend,threshold,legend,visualization | Multi-line chart for time-series data, thresholds, advanced tooltips, Recharts-based  | src/app/widgets/timeserieslinegraph/README.md    |
| title                  | display    | title,heading,theme,alignment,styling                | Flexible, theme-aware title/header with configurable size, alignment, styling         | src/app/widgets/title/README.md                  |

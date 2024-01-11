# Arrays are called lists

import os
import re
from subprocess import call

class bcolors:
    GRAY = '\33[30m' # Gray
    HEADER = '\033[95m' # Purple
    OKBLUE = '\033[94m' # Blue
    OKCYAN = '\033[96m' # Cyan
    OKGREEN = '\033[92m' # Green
    WARNING = '\033[93m' # Yellow
    FAIL = '\033[91m' # Red
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear():
    # check and make call for specific operating system
    _ = call('clear' if os.name == 'posix' else 'cls')

def printCreatingFilename(fileName):
    print(bcolors.OKCYAN + 'Creating' + bcolors.ENDC + bcolors.BOLD + ' %s ' % (fileName) + bcolors.ENDC )

def askUser(question, example):
    return input('~ ' + bcolors.HEADER + '%s' % (question) + bcolors.GRAY + ' (%s)' % (example) + bcolors.ENDC +': ' + bcolors.BOLD + bcolors.ENDC)

def main():
    clear()

    title = 'React Component builder'
    componentName = ''
    
    print(title)
    print('=' * len(title))
    print("\n")

    componentName = askUser('Please enter the name of your component', 'CapitalCase').split()

    parsedComponentName = ''

    if len(componentName) == 1:
        for word in re.findall('.[^A-Z]*', componentName[0]):
            parsedComponentName += word.capitalize()
    elif len(componentName) > 1:
        for word in componentName:
             parsedComponentName += word.capitalize()

    if os.path.exists('%s' % (parsedComponentName)):
        print(bcolors.FAIL + 'Folder for %s already exists!' % (parsedComponentName))
        exit()
    else:
        os.makedirs('%s' % (parsedComponentName))
        print(bcolors.OKGREEN + 'Folder created!')

    tsxFilename = parsedComponentName + '.tsx'
    auxFilenames = ['utils', 'hooks', 'constants', 'index']
    
    print('\n')
    printCreatingFilename(parsedComponentName + '.tsx')

    tsxContent = '''import styles from './%s.module.scss'

interface Props {
    arg: string;
}
    
function %s({arg}: Props) {
    return (
        <div className={styles.container}>%s</div>
    )
}
    
export default %s''' % (parsedComponentName, parsedComponentName, parsedComponentName, parsedComponentName)

    tsx = open(parsedComponentName + '/' + tsxFilename, 'w')
    tsx.write(tsxContent)
    tsx.close()

    printCreatingFilename(parsedComponentName + '.module.scss')

    scss = open(parsedComponentName + '/' + parsedComponentName + '.module.scss', 'w')
    scss.write('.container {\n  border: 1px solid red;\n}')
    scss.close()

    print('\n')
    print(bcolors.OKCYAN + 'Creating aux files')
    print('\n')

    for file in auxFilenames:
        printCreatingFilename(file + '.ts')
        output = open(parsedComponentName + '/' + file + '.ts', 'w')
        output.write('// %s.ts file' % (file) if file != 'index' else "import %s from './%s'\n\nexport {%s}" % (parsedComponentName, parsedComponentName, parsedComponentName))
        output.close()

    print('\n')
    print(bcolors.OKGREEN + 'Ready!')

if __name__ == "__main__": 
    main()
# Trace the evolution from Java Servlets to the Spring Boot framework. Explain the problems each iteration aimed to solve, and detail the core functionalities of the Spring framework along with essential knowledge required for developers working with it.

# Deep Research Report: The Evolution from Java Servlets to Spring Boot

## Executive Summary

This report traces the technological evolution of Java web application development, beginning with the foundational Java Servlet API and culminating in the modern Spring Boot framework. The central theme of this evolution is a persistent drive to increase developer productivity by abstracting complexity, reducing boilerplate code, and improving the testability of application logic.

Initially, Java Servlets provided a significant improvement over the process-per-request model of CGI scripts by introducing a more efficient, thread-based architecture. However, the Servlet/JSP model suffered from tight coupling to the Servlet API and a tendency to mix business logic with presentation code, making applications difficult to test and maintain.

Subsequent frameworks like Apache Struts 1 introduced the Model-View-Controller (MVC) pattern, providing a crucial separation of concerns. Yet, Struts 1 controllers remained tightly coupled to the Servlet API, complicating unit testing. In parallel, the Enterprise JavaBeans (EJB) 2.x specification offered a powerful but heavyweight and complex component model, burdened by excessive XML configuration and difficult testing procedures.

The Spring Framework emerged as a lightweight alternative to EJB, championing the principles of Inversion of Control (IoC) and Dependency Injection (DI). By managing Plain Old Java Objects (POJOs), Spring decoupled business logic from the underlying framework and infrastructure. Spring MVC represented a major breakthrough in testability by allowing controllers to be written as simple POJOs, free from direct Servlet API dependencies.

Finally, Spring Boot addressed the remaining complexities of dependency management and configuration within the Spring ecosystem itself. By introducing "convention over configuration," auto-configuration, starter dependencies, and embedded servers, Spring Boot radically simplified the process of building and deploying production-ready, stand-alone Spring applications.

## 1. The Foundation: Java Servlets and JSP

### 1.1 From CGI to a Thread-Based Model
Before Java Servlets, the Common Gateway Interface (CGI) was the standard for generating dynamic web content. CGI operated on a process-based model, launching an entirely new operating system process for every incoming request. This approach was resource-intensive and inefficient.

Java Servlets offered a superior, thread-based architecture. Instead of a new process, the servlet container creates a new, lightweight thread to handle each request. This allows servlets to run within the server process, share data more efficiently, and manage resources more effectively than CGI scripts.

### 1.2 The Servlet Lifecycle and Request-Response Model
A Java Servlet's lifecycle is managed by the servlet container and defined by three key methods:
*   **`init()`**: Called only once when the servlet instance is first created to perform one-time initialization.
*   **`service()`**: Called for every incoming request. The container creates `HttpServletRequest` and `HttpServletResponse` objects and passes them to this method, which contains the core request-handling logic. A single servlet instance handles multiple requests concurrently via multiple threads executing the `service()` method.
*   **`destroy()`**: Called only once when the servlet is taken out of service, allowing for resource cleanup.

### 1.3 View Technology and Early Challenges
JavaServer Pages (JSP) was introduced as a view technology to separate presentation from business logic. The intent was to allow developers to embed Java code snippets, called "scriptlets," within HTML pages. However, this often led to "scriptlet abuse," where extensive business logic (e.g., database calls, calculations) was written directly into JSP files. This practice defeated the goal of separation of concerns, leading to tightly coupled, difficult-to-maintain, and untestable code.

### 1.4 Baseline Example: The Tightly Coupled `LoginServlet`
A typical early `LoginServlet` demonstrates the problems of this monolithic model:
*   **Tight Coupling to Servlet API**: Business logic is directly tied to the Servlet API through the manual use of `request.getParameter()` to retrieve form data.
*   **Manual State Management**: Session management is handled manually by retrieving an `HttpSession` from the request (`request.getSession()`), storing attributes (`session.setAttribute()`), and invalidating it (`session.invalidate()`).
*   **Direct Object Instantiation**: Dependencies, services, and other objects are instantiated directly within the servlet's methods (e.g., `new Cookie(...)`).

This tight coupling makes unit testing extremely difficult. To test the logic within the `doPost` method, a developer must mock the `HttpServletRequest` and `HttpServletResponse` objects, a complex and cumbersome process.

```java
// A representative example of a monolithic servlet
protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    // 1. Direct parameter retrieval from the Servlet API
    String user = request.getParameter("user");
    String pwd = request.getParameter("pwd");

    // Business Logic
    if("admin".equals(user) && "password".equals(pwd)){
        // 2. Manual session management
        HttpSession session = request.getSession();
        session.setAttribute("user", "Pankaj");
        session.setMaxInactiveInterval(30*60);

        // 3. Direct instantiation of objects
        Cookie userName = new Cookie("user", user);
        response.addCookie(userName);

        response.sendRedirect("LoginSuccess.jsp");
    } else {
        // ... error handling
    }
}
```

## 2. The First Step Towards Separation: Apache Struts 1

### 2.1 Introducing the MVC Pattern
Apache Struts 1 was a pioneering open-source framework that popularized the Model-View-Controller (MVC) design pattern for Java web applications. By separating concerns, it provided a significant architectural improvement over the ad-hoc Servlet/JSP model.

The components of Struts 1 map to the MVC roles as follows:
*   **Controller**: The `ActionServlet` acts as a central "front controller" that intercepts all requests. Based on the `struts-config.xml` file, it delegates the request to a specific `Action` class, which contains the business logic to handle the user's action.
*   **Model**: The `ActionForm` bean represents the model. It automatically captures and validates user input from HTML forms, eliminating the need for manual `request.getParameter()` calls. The business services called by the `Action` class are also part of the model layer.
*   **View**: JSPs serve as the view. After an `Action` class completes its processing, it returns a result that Struts uses to forward the request to the appropriate JSP for rendering the response.

### 2.2 Testability Limitations Due to Servlet API Coupling
While Struts 1 introduced a much-needed structure, it did not fully solve the problem of testability. The `Action` class, the core of the controller logic, remained tightly coupled to the Servlet API. The definitive signature of its primary method is:

`public ActionForward execute(ActionMapping mapping, ActionForm form, HttpServletRequest request, HttpServletResponse response)`

This signature reveals the core limitation: any business logic inside the `execute` method has a direct dependency on `HttpServletRequest` and `HttpServletResponse`. Consequently, unit testing a Struts 1 `Action` class still required developers to create and manage mock implementations of these Servlet API objects, making the testing process complex and contradicting the goal of isolating business logic from the web container.

## 3. The Enterprise Complexity Problem: EJB 2.x

While frameworks like Struts tackled web-layer issues, Enterprise JavaBeans (EJB) was the dominant specification for building large-scale, transactional enterprise applications. However, the EJB 2.x iteration was widely criticized for its "heavyweight" nature and excessive complexity.

Key pain points of EJB 2.x development included:
*   **Required Interfaces**: Developers were forced to create home and remote interfaces for their components, adding significant boilerplate.
*   **Heavyweight Component Model**: EJB components were not simple Java objects; they had to implement specific framework interfaces (e.g., `javax.jms.MessageListener`) and were tightly coupled to the EJB container.
*   **The "XML Configuration Nightmare"**: Every EJB required a verbose and complex XML deployment descriptor (`ejb-jar.xml`). A descriptor for a single, simple bean could easily exceed 200 lines of code [https://medium.com/javarevisited/jakarta-ee-12-the-death-of-enterprise-javabeans-4132a0ab6a9d].
*   **Difficult Unit Testing**: Because components were coupled to the EJB specification and required a container to function, unit testing them in isolation was notoriously difficult [https://stackoverflow.com/questions/5337779/unit-testing-ejb-2-x].

## 4. A Lightweight Revolution: The Spring Framework

The Spring Framework, created by Rod Johnson and based on the concepts in his book *Expert One-on-One J2EE Development Without EJB*, emerged as a direct response to the complexity of EJB 2.x. It introduced a simpler, lightweight, POJO-based model for enterprise development.

### 4.1 Inversion of Control and Dependency Injection
The foundation of Spring is the principle of **Inversion of Control (IoC)**, implemented via **Dependency Injection (DI)**.
*   **Inversion of Control**: Instead of application components controlling their own lifecycle and dependencies (e.g., using the `new` keyword), control is inverted to an external container.
*   **Dependency Injection**: The container is responsible for "injecting" the required dependencies into a component when it is created.

The Spring IoC container (represented by the `ApplicationContext` or `BeanFactory`) manages the entire lifecycle of application objects, known as "beans." By managing dependencies externally, Spring promotes loose coupling between components. This loose coupling was a direct solution to the tight coupling and testing difficulties prevalent in both the Servlet model and EJB 2.x.

### 4.2 The POJO-Based Model
Spring championed a Plain Old Java Object (POJO)-based programming model. Unlike EJB 2.x components, Spring beans are simple Java classes with no need to implement framework-specific interfaces. This decouples the business logic from the Spring infrastructure, making the code more flexible and significantly easier to test as a standalone object.

## 5. Core Functionalities and the Testability Breakthrough

### 5.1 Spring MVC and the Decoupled Controller
The Spring MVC framework is built around a central `DispatcherServlet` that, like in Struts, acts as a front controller. However, its approach to controller design marked a major leap forward in testability. A Spring MVC controller is a simple POJO, and its handler methods have flexible signatures that use annotations to bind request data, completely avoiding a direct dependency on the Servlet API.

### 5.2 The Definitive Comparison: Struts 1 vs. Spring MVC Testability
The contrast between the method signatures of a Struts 1 controller and a Spring MVC controller clearly illustrates the evolution in testability.

*   **Struts 1 `Action.execute` Signature**:
    `public ActionForward execute(ActionMapping mapping, ActionForm form, HttpServletRequest request, HttpServletResponse response)`
    *   **Impact**: The presence of `HttpServletRequest` forces the developer to provide a mock version of it during a unit test.

*   **Spring MVC Controller Signature**:
    ```java
    @GetMapping("/products")
    public ResponseEntity getProductById(@RequestParam Long id) {
        // Method logic to retrieve product details
    }
    ```
    *   **Impact**: The controller method has no dependency on any Servlet API class. The `@RequestParam` annotation tells Spring to extract the `id` parameter from the HTTP request and pass it as a simple `Long` to the method. The controller can be instantiated as a POJO (`new ProductController()`), and the `getProductById` method can be called directly in a unit test by simply passing a `Long` value, with no mocking required.

This decoupling allows business logic within the controller to be tested in complete isolation, a revolutionary improvement over previous frameworks.

### 5.3 AOP, Data Access, and Security
Spring provided comprehensive solutions for other common enterprise needs:
*   **Aspect-Oriented Programming (AOP)**: Spring AOP allows developers to separate cross-cutting concerns (e.g., logging, security, transactions) from business logic. It works by creating dynamic proxies (either JDK or CGLIB) that wrap the target object and apply the aspect's behavior before or after method execution.
*   **Data Access and Transactions**: The `JdbcTemplate` drastically reduces the boilerplate code associated with standard JDBC by automatically managing resources like connections. Furthermore, Spring's declarative transaction management, using the `@Transactional` annotation, simplifies data consistency by allowing developers to define transaction boundaries without writing manual `commit` or `rollback` logic.
*   **Spring Security**: A dedicated module provides robust authentication and authorization services, implemented as a chain of servlet filters to protect web applications against common vulnerabilities.

### 5.4 Evolution of Configuration: From XML to Annotations
Early versions of Spring relied heavily on XML files (`applicationContext.xml`) for configuration. While powerful, this led to a problem known as "XML Hell," where configuration became verbose and difficult to manage. Spring evolved to address this by introducing:
*   **Annotation-based Configuration**: Annotations like `@Component`, `@Service`, and `@Autowired` allowed developers to define beans and their dependencies directly in the Java code.
*   **Java-based Configuration**: Classes annotated with `@Configuration` and methods with `@Bean` provided a type-safe, fully programmatic way to configure the Spring container, largely replacing XML.

## 6. The Final Leap: Spring Boot and Convention over Configuration

Despite its power, setting up a new Spring project still involved significant boilerplate: configuring the `DispatcherServlet`, managing a complex web of dependencies, and setting up data sources and transaction managers. Spring Boot was created to solve these remaining challenges.

Its core philosophy is **"Convention over Configuration."** It makes intelligent, opinionated assumptions about how to configure an application, drastically reducing the amount of manual setup required.

Key features of Spring Boot include:
*   **Auto-Configuration**: Spring Boot automatically configures the application based on the JARs present on the classpath. For example, if it detects `spring-webmvc.jar`, it automatically configures a `DispatcherServlet` and other web-related beans.
*   **Starter Dependencies**: These are convenient dependency descriptors that bundle common dependencies together. For example, including `spring-boot-starter-web` in a project provides all the necessary dependencies for building a web application, including Spring MVC, validation, and an embedded Tomcat server.
*   **Embedded Servers**: Spring Boot applications bundle an embedded web server (like Tomcat, Jetty, or Undertow) by default. This allows the application to be run as a standalone executable JAR file (`java -jar app.jar`), eliminating the need to deploy a traditional WAR file to an external application server.

## 7. Essential Knowledge for the Modern Spring Developer

A developer working with the modern Spring ecosystem today is expected to have proficiency in the following areas:
*   **Core Annotations**: Mastery of key annotations for dependency injection (`@Autowired`, `@Component`), configuration (`@Configuration`, `@Bean`), web development (`@RestController`, `@GetMapping`), and data access (`@Entity`, `@Transactional`).
*   **Application Properties**: Understanding the property hierarchy and how to configure the application using `application.properties` or `application.yml` files.
*   **Build Tools and Dependency Management**: Proficiency with Maven or Gradle, specifically in managing Spring Boot starter dependencies.
*   **RESTful API Design**: Designing and building REST APIs using Spring MVC or its reactive counterpart, Spring WebFlux.
*   **Data Persistence**: Interacting with databases using Spring Data JPA.
*   **Testing**: Writing unit and integration tests using frameworks like JUnit, Mockito, and the `spring-boot-starter-test` package.

## 8. Conclusion and Outlook

The journey from Java Servlets to Spring Boot is a clear narrative of progressive abstraction and simplification. Each technological iteration solved critical problems of the last, moving from manual, low-level request handling to a highly automated, convention-driven framework. The primary goals have remained consistent: reduce boilerplate, decouple application logic from the underlying infrastructure, and enhance the testability of code. This evolution has made Java a highly productive platform for building robust, scalable, and maintainable enterprise and cloud-native applications.

While data on a direct comparison with contemporary frameworks like Quarkus and Micronaut, or the future outlook regarding reactive programming (WebFlux) and native compilation with GraalVM, was not available in the provided research, these areas represent the ongoing evolution of the Java ecosystem. They continue the trend of optimizing for performance, resource efficiency, and developer experience in a cloud-native world.

---
## References

*   [http://letssharejavaexperience.blogspot.com/2012/12/ejb-2x-vs-ejb-30-vs-ejb-31.html](http://letssharejavaexperience.blogspot.com/2012/12/ejb-2x-vs-ejb-30-vs-ejb-31.html)
*   [http://web.cs.ucla.edu/classes/winter15/cs144/projects/java/session/](http://web.cs.ucla.edu/classes/winter15/cs144/projects/java/session/)
*   [https://coderanch.com/t/56109/frameworks/understand-ActionServlet](https://coderanch.com/t/56109/frameworks/understand-ActionServlet)
*   [https://codesignal.com/learn/courses/introduction-to-spring-boot-and-spring-core-with-kotlin/lessons/bean-scopes-and-lifecycle](https://codesignal.com/learn/courses/introduction-to-spring-boot-and-spring-core-with-kotlin/lessons/bean-scopes-and-lifecycle)
*   [https://devcookies.medium.com/the-scope-of-beans-in-spring-boot-a-comprehensive-guide-ca4de7c531f3](https://devcookies.medium.com/the-scope-of-beans-in-spring-boot-a-comprehensive-guide-ca4de7c531f3)
*   [https://itidoltechnologies.com/blog/java-2025-trends-shaping-enterprise-application-development/](https://itidoltechnologies.com/blog/java-2025-trends-shaping-enterprise-application-development/)
*   [https://javadoc.io/doc/org.apache.struts/struts-core/1.3.8/org/apache/struts/action/class-use/ActionMapping.html](https://javadoc.io/doc/org.apache.struts/struts-core/1.3.8/org/apache/struts/action/class-use/ActionMapping.html)
*   [https://medium.com/@meowmbaikar/servlet-session-management-and-redirection-0497c5e8b40a](https://medium.com/@meowmbaikar/servlet-session-management-and-redirection-0497c5e8b40a)
*   [https://medium.com/@niitwork0921/understanding-servlet-life-cycle-in-java-eba0e73ca379](https://medium.com/@niitwork0921/understanding-servlet-life-cycle-in-java-eba0e73ca379)
*   [https://medium.com/@sharmapraveen91/mastering-spring-aop-the-ultimate-guide-for-2025-55a146c8204c](https://medium.com/@sharmapraveen91/mastering-spring-aop-the-ultimate-guide-for-2025-55a146c8204c)
*   [https://medium.com/@umeshcapg/avamastering-aop-in-spring-boot-sta-0b9aef096c45](https://medium.com/@umeshcapg/avamastering-aop-in-spring-boot-sta-0b9aef096c45)
*   [https://medium.com/@viranthrocky/why-jdbctemplate-still-deserves-a-place-in-modern-applications-over-jpa-f0b8f899ddf6](https://medium.com/@viranthrocky/why-jdbctemplate-still-deserves-a-place-in-modern-applications-over-jpa-f0b8f899ddf6)
*   [https://medium.com/javarevisited/jakarta-ee-12-the-death-of-enterprise-javabeans-4132a0ab6a9d](https://medium.com/javarevisited/jakarta-ee-12-the-death-of-enterprise-javabeans-4132a0ab6a9d)
*   [https://stackoverflow.com/questions/1835764/java-servlet-session-management-how-to-create-session-for-login](https://stackoverflow.com/questions/1835764/java-servlet-session-management-how-to-create-session-for-login)
*   [https://stackoverflow.com/questions/24501341/struts-1-entry-actionform-inputs-from-any-action-class](https://stackoverflow.com/questions/24501341/struts-1-entry-actionform-inputs-from-any-action-class)
*   [https://stackoverflow.com/questions/38693768/what-is-the-benefit-of-using-jdbc-template](https://stackoverflow.com/questions/38693768/what-is-the-benefit-of-using-jdbc-template)
*   [https://stackoverflow.com/questions/3894088/what-is-the-lifecycle-of-a-httpservlet](https://stackoverflow.com/questions/3894088/what-is-the-lifecycle-of-a-httpservlet)
*   [https://stackoverflow.com/questions/5337779/unit-testing-ejb-2-x](https://stackoverflow.com/questions/5337779/unit-testing-ejb-2-x)
*   [https://stackoverflow.com/questions/5808585/basic-flow-of-struts](https://stackoverflow.com/questions/5808585/basic-flow-of-struts)
*   [https://struts.apache.org/getting-started/processing-forms](https://struts.apache.org/getting-started/processing-forms)
*   [https://www.codeproject.com/articles/Dynamic-Proxy-in-Spring-A-Comprehensive-Guide-with](https://www.codeproject.com/articles/Dynamic-Proxy-in-Spring-A-Comprehensive-Guide-with)
*   [https://www.codingshuttle.com/spring-proxy-and-internal-working-of-aop](https://www.codingshuttle.com/spring-proxy-and-internal-working-of-aop)
*   [https://www.d.umn.edu/~tcolburn/cs4531/struts/api/org/apache/struts/action/class-use/ActionMapping.html](https://www.d.umn.edu/~tcolburn/cs4531/struts/api/org/apache/struts/action/class-use/ActionMapping.html)
*   [https://www.digitalocean.com/community/tutorials/java-session-management-servlet-httpsession-url-rewriting](https://www.digitalocean.com/community/tutorials/java-session-management-servlet-httpsession-url-rewriting)
*   [https://www.dineshonjava.com/understanding-aop-proxies-chapter-31/](https://www.dineshonjava.com/understanding-aop-proxies-chapter-31/)
*   [https://www.everand.com/book/254392114/Beginning-Spring](https://www.everand.com/book/254392114/Beginning-Spring)
*   [https://www.geeksforgeeks.org/java/singleton-and-prototype-bean-scopes-in-java-spring/](https://www.geeksforgeeks.org/java/singleton-and-prototype-bean-scopes-in-java-spring/)
*   [https://www.infoq.com/news/2025/03/day-two-java-one-2025/](https://www.infoq.com/news/2025/03/day-two-java-one-2025/)
*   [https://www.infoworld.com/article/2163165/accelerate-ejb-2-0-development-with-ejbgen.html](https://www.infoworld.com/article/2163165/accelerate-ejb-2-0-development-with-ejbgen.html)
*   [https://www.linkedin.com/posts/dasa-shekar-8b228722b_java-day-activity-7374393784593395712-b7zR](https://www.linkedin.com/posts/dasa-shekar-8b228722b_java-day-activity-7374393784593395712-b7zR)
*   [https://www.oschina.net/uploads/doc/struts-1.3.9/org/apache/struts/action/class-use/ActionForm.html](https://www.oschina.net/uploads/doc/struts-1.3.9/org/apache/struts/action/class-use/ActionForm.html)
*   [https://www.quora.com/Is-the-Spring-Framework-less-or-more-difficult-than-the-problems-it-wants-to-solve-Isn%E2%80%99t-it-overcomplicated](https://www.quora.com/Is-the-Spring-Framework-less-or-more-difficult-than-the-problems-it-wants-to-solve-Isn%E2%80%99t-it-overcomplicated)
*   [https://www.quora.com/What-does-the-Java-Servlet-Container-state](https://www.quora.com/What-does-the-Java-Servlet-Container-state)
*   [https://www.quora.com/What-is-Spring-Framework-and-its-architecture](https://www.quora.com/What-is-Spring-Framework-and-its-architecture)
*   [https://www.quora.com/Why-do-you-think-people-like-the-Spring-Framework](https://www.quora.com/Why-do-you-think-people-like-the-Spring-Framework)
*   [https://www.scribd.com/document/105974072/Struts-1](https://www.scribd.com/document/105974072/Struts-1)
*   [https://www.scribd.com/document/344954456/Struts-1-doc](https://www.scribd.com/document/344954456/Struts-1-doc)
*   [https://www.scribd.com/document/6569879/The-Complete-Spring-Tutorial](https://www.scribd.com/document/6569879/The-Complete-Spring-Tutorial)
*   [https://www.upgrad.com/blog/servlet-life-cycle-in-java/](https://www.upgrad.com/blog/servlet-life-cycle-in-java/)
*   [https://www.youtube.com/watch?v=RJYxr7ThD00](https://www.youtube.com/watch?v=RJYxr7ThD00)
*   [https://www.zzrose.com/tech/pmr_sweSimpleStruts1xExample.html](https://www.zzrose.com/tech/pmr_sweSimpleStruts1xExample.html)

## Citations 
- https://www.studocu.com/in/document/university-of-madras/computer-science-msc/java-servlets-and-cgi-key-differences-architecture-and-functionality/126230455
- https://studyglance.in/servlet/display.php?tno=3&topic=CGI-vs-Servlet
- https://www.edureka.co/blog/java-servlets
- https://www.geeksforgeeks.org/java/difference-between-java-servlet-and-cgi/
- https://www.oreilly.com/library/view/learning-java/1565927184/ch12s04.html
- https://www.oracle.com/java/technologies/javaserver-white-paper.html
- https://stackoverflow.com/questions/3177733/how-can-i-avoid-java-code-in-jsp-files-using-jsp-2
- https://medium.com/@vtambavekar239/why-jsp-servlets-still-matter-in-modern-web-development-9ccf2330e794
- https://www.quora.com/What-is-JSP-used-for-Why-have-people-stopped-using-it
- https://www.altdigital.tech/resources/altdigitalpedia/java-server-pages-jsp
- https://www.upgrad.com/blog/servlet-life-cycle-in-java/
- https://www.youtube.com/watch?v=RJYxr7ThD00
- https://www.quora.com/What-does-the-Java-Servlet-Container-state
- https://stackoverflow.com/questions/3894088/what-is-the-lifecycle-of-a-httpservlet
- https://medium.com/@niitwork0921/understanding-servlet-life-cycle-in-java-eba0e73ca379
- https://struts.apache.org/announce-2025
- https://www.scribd.com/document/344954456/Struts-1-doc
- https://stackoverflow.com/questions/5808585/basic-flow-of-struts
- https://coderanch.com/t/56109/frameworks/understand-ActionServlet
- https://www.zzrose.com/tech/pmr_sweSimpleStruts1xExample.html
- https://struts.apache.org/getting-started/processing-forms
- https://stackoverflow.com/questions/226977/what-is-loose-coupling-please-provide-examples
- https://dev.to/priyankachettri/overcoming-tight-coupling-in-oops-with-effective-solutions-3d3g
- https://naveen-metta.medium.com/untangling-the-knot-solving-the-coupling-problem-in-java-8c7460b8338c
- https://struts.apache.org/getting-started/coding-actions
- https://viblo.asia/p/struts-1-components-ZabG91kmGzY6
- http://ducmanhphan.github.io/2019-03-11-How-to-configure-in-Struts-1-framework/
- https://www.scribd.com/document/145610496/Struts
- https://medium.com/@SachinPandeyOnline/advanced-java-struts-components-8b8d64fa4c74
- https://www.infoq.com/news/2025/03/day-two-java-one-2025/
- https://itidoltechnologies.com/blog/java-2025-trends-shaping-enterprise-application-development/
- https://stackoverflow.com/questions/5337779/unit-testing-ejb-2-x
- https://www.ibm.com/docs/en/rational-soft-arch/9.7.0?topic=reference-limitations-ejb-1x-2x-development-tools
- https://www.infoworld.com/article/2163165/accelerate-ejb-2-0-development-with-ejbgen.html
- http://letssharejavaexperience.blogspot.com/2012/12/ejb-2x-vs-ejb-30-vs-ejb-31.html
- https://medium.com/javarevisited/jakarta-ee-12-the-death-of-enterprise-javabeans-4132a0ab6a9d
- https://blog.softwaremill.com/the-apache-struts-an-open-source-mvc-framework-for-creating-elegant-modern-java-web-1ae882f0a550
- https://www.youtube.com/watch?v=MDHj4vgKY6Q
- https://moldstud.com/articles/p-mastering-mvc-architecture-with-jsp-in-java-ee-applications-a-comprehensive-guide
- https://www.scribd.com/document/6569879/The-Complete-Spring-Tutorial
- https://www.quora.com/Is-the-Spring-Framework-less-or-more-difficult-than-the-problems-it-wants-to-solve-Isn%E2%80%99t-it-overcomplicated
- https://www.quora.com/What-is-Spring-Framework-and-its-architecture
- https://www.quora.com/Why-do-you-think-people-like-the-Spring-Framework
- https://www.everand.com/book/254392114/Beginning-Spring
- https://stackoverflow.com/questions/72616542/in-spring-dependency-injection-how-does-tight-coupling-hurt-the-unit-testing
- https://medium.com/@bolot.89/understanding-beanfactory-and-applicationcontext-in-spring-boot-a-deep-dive-f7f92f3a16f5
- https://www.quora.com/Why-do-developers-use-Spring-Framework-for-dependency-injection-Why-not-use-plain-Java-code-and-instantiate-the-bean-classes-just-like-any-other-Java-instance-e-g-new-SomeService-obj1-obj2
- https://www.linkedin.com/posts/lahiru-liyanapathirana_confused-about-springs-ioc-containers-lets-activity-7335635140485726208-BkLa
- https://kamilmazurek.pl/spring-beans-explained
- https://www.baeldung.com/spring-bean-vs-ejb
- https://dev.to/isaactony/comparing-pojos-javabeans-and-spring-beans-in-detail-3f1
- https://bill.burkecentral.com/2012/03/13/java-ee-wins-over-spring/
- https://www.geeksforgeeks.org/java/difference-between-ejb-and-spring/
- https://www.quora.com/What-are-the-differences-between-EJB-Enterprise-JavaBeans-and-the-Spring-Framework-in-Java-Which-one-is-better-Why
- https://quizlet.com/study-guides/overview-of-spring-framework-modules-and-features-81734674-a2a2-4127-a176-04010e275fc5
- https://dev.to/pablocavalcanteh/spring-framework-overview-of-main-modules-and-annotations-4b12
- https://medium.com/@yunussiddiqui55/important-spring-framework-modules-28ff03cfdd29
- https://www.linkedin.com/pulse/introduction-spring-framework-k%C4%81sh%C4%81n-asim-knude
- https://www.quora.com/What-are-the-different-modules-of-spring
- https://www.quora.com/Why-do-we-use-Spring-Framework-Can-anybody-explain-this-in-a-non-technical-kind-of-way-with-some-examples
- https://www.altdigital.tech/resources/altdigitalpedia/spring
- https://anilr8.medium.com/mastering-spring-framework-core-concepts-best-practices-and-advanced-techniques-d9ab6f90cc80
- https://www.geeksforgeeks.org/advance-java/spring-ioc-container/
- https://www.geeksforgeeks.org/advance-java/introduction-to-spring-framework/
- https://learncodewithdurgesh.com/tutorials/spring-boot-tutorials/spring-mvc-architecture-dispatcherservlet-flow
- https://www.codingshuttle.com/spring-boot-handbook/spring-mvc-architecture
- https://www.upgrad.com/blog/spring-mvc-flow-diagram/
- https://www.youtube.com/watch?v=Cu3mHxv8-To
- https://javalaunchpad.com/introduction-to-spring-mvc-architecture/
- https://www.digitalocean.com/community/tutorials/java-session-management-servlet-httpsession-url-rewriting
- https://www.java4s.com/java-servlet-tutorials/example-of-request-getparameter-retrieve-parameters-from-html-form/
- https://stackoverflow.com/questions/1835764/java-servlet-session-management-how-to-create-session-for-login
- http://web.cs.ucla.edu/classes/winter15/cs144/projects/java/session/
- https://medium.com/@meowmbaikar/servlet-session-management-and-redirection-0497c5e8b40a
- https://stackoverflow.com/questions/849051/java-struts-1-forward-from-action-to-action-passing-data-through-actionforms
- https://www.scribd.com/document/6932490/Apache-Struts-Handling-Request-Parameters-With-Form-Beans-Struts-1-2-Version
- https://forums.oracle.com/ords/apexds/post/using-struts-action-class-and-servlet-together-4126
- https://coderanch.com/t/52756/frameworks/pass-parameter-struts
- https://www.laliluna.de/articles/posts/struts-forms-overview.html
- https://www.javawebtutor.com/articles/struts/struts_action.php
- https://www.scribd.com/document/145610496/Struts
- https://svn.apache.org/repos/asf/struts/archive/trunk/struts-doc-1.1/api/org/apache/struts/action/ActionServlet.html
- https://struts.apache.org/getting-started/coding-actions
- https://huongdanjava.com/introduction-to-apache-struts-1.html
- https://medium.com/@sharmapraveen91/mastering-spring-aop-the-ultimate-guide-for-2025-55a146c8204c
- https://www.codeproject.com/articles/Dynamic-Proxy-in-Spring-A-Comprehensive-Guide-with
- https://medium.com/@umeshcapg/avamastering-aop-in-spring-boot-sta-0b9aef096c45
- https://www.codingshuttle.com/spring-boot-handbook/spring-proxy-and-internal-working-of-aop
- https://www.dineshonjava.com/understanding-aop-proxies-chapter-31/
- https://stackoverflow.com/questions/6627033/spring-mvc-and-handler-methods-with-pojos
- https://levelup.gitconnected.com/spring-rest-api-pathvariable-requestparam-requestbody-and-input-validation-e6a6ebccd6ad
- https://www.baeldung.com/spring-requestparam-vs-pathvariable
- https://stackoverflow.com/questions/57905483/combining-pathvariable-and-requestbody
- https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-controller/ann-methods/requestparam.html
- https://naveen-metta.medium.com/understanding-requestparam-vs-pathvariable-in-spring-a-comprehensive-guide-41fb956e20f6
- https://www.educba.com/spring-vs-struts/
- https://topic.alibabacloud.com/a/comparison-between-struts-and-spring-mvc-font-classtopic-s-color00c1deframeworksfont_1_27_32689037.html
- https://stackoverflow.com/questions/6173009/difference-between-spring-mvc-and-struts-mvc
- https://bluebirdinternational.com/spring-framework-vs-struts/
- https://www.geeksforgeeks.org/java/spring-vs-struts-in-java/
- https://stackoverflow.com/questions/12795100/could-requestmapping-and-strutss-mapping-be-used-in-the-same-time
- https://www.urbanpro.com/dot-net-mvc/which-one-is-better-spring-mvc-or-struts
- https://devcookies.medium.com/the-scope-of-beans-in-spring-boot-a-comprehensive-guide-ca4de7c531f3
- https://dev.to/isaactony/singleton-and-prototype-spring-bean-scopes-a-detailed-exploration-1gpl
- https://codesignal.com/learn/courses/introduction-to-spring-boot-and-spring-core-with-kotlin/lessons/bean-scopes-and-lifecycle
- https://www.geeksforgeeks.org/java/singleton-and-prototype-bean-scopes-in-java-spring/
- https://www.youtube.com/watch?v=8M8V7D-Y2co
- https://javadoc.io/static/org.apache.struts/struts-core/1.3.10/index.html?org/apache/struts/action/package-summary.html
- https://javadoc.io/static/org.apache.struts/struts-core/1.3.8/index.html?org/apache/struts/action/Action.html
- http://tool.oschina.net/uploads/apidocs/struts-1.3.10/org/apache/struts/action/package-summary.html
- https://svn.apache.org/repos/asf/struts/archive/trunk/struts-doc-1.1/api/org/apache/struts/action/Action.html
- https://struts.apache.org/core-developers/action-configuration
- https://www.linkedin.com/posts/dasa-shekar-8b228722b_java-day-activity-7374393784593395712-b7zR
- https://medium.com/@viranthrocky/why-jdbctemplate-still-deserves-a-place-in-modern-applications-over-jpa-f0b8f899ddf6
- https://hackernoon.com/comparing-database-integration-approaches-in-spring-boot-spring-data-jpa-vs-spring-jdbc-vs-jooq
- https://stackoverflow.com/questions/38693768/what-is-the-benefit-of-using-jdbc-template
- https://www.geeksforgeeks.org/springboot/spring-boot-spring-jdbc-vs-spring-data-jdbc/
- https://stackoverflow.com/questions/24501341/struts-1-entry-actionform-inputs-from-any-action-class
- https://javadoc.io/doc/org.apache.struts/struts-core/1.3.8/org/apache/struts/action/class-use/ActionMapping.html
- https://www.oschina.net/uploads/doc/struts-1.3.9/org/apache/struts/action/class-use/ActionForm.html
- https://www.scribd.com/document/105974072/Struts-1
- https://www.d.umn.edu/~tcolburn/cs4531/struts/api/org/apache/struts/action/class-use/ActionMapping.html
- https://withoutbook.com/InterviewQuestionAnswer.php?tech=4&quesId=774&s=Struts%20Interview%20Questions%20and%20Answers
- https://www.baeldung.com/spring-programmatic-transaction-management
- https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative.html
- https://www.marcobehler.com/guides/spring-transaction-management-transactional-in-depth
- https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/annotations.html
- https://www.sivalabs.in/blog/spring-boot-database-transaction-management-tutorial/